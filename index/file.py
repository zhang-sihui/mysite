""" 文件上传与下载
1.上传大小检查
2.下载次数统计
"""

import os
from django.db.models import Sum
from django.http import FileResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.encoding import escape_uri_path
from django.shortcuts import render
from .models import File
from .common import translate_message
from . import base_dir


# Create your views here.

def files(request):
    """ 以文件夹里的文件为主, 显示实际存在的文件 """
    file_dir = os.path.join(base_dir, 'files')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    files = os.listdir(file_dir)
    if not files:
        not_files_message = translate_message('No files currently')
        return render(request, 'index/file.html', locals())
    else:
        not_sorted_files_data = []
        for file_name in files:
            file_info = File.objects.get(file_name=file_name)
            file_data = (file_info.id, file_name + ' -- ' + str(os.path.getsize(file_dir + '/' + file_name) // 1024) + ' KB', 
                         file_info.downloads, file_info.pub_date)
            not_sorted_files_data.append(file_data)
        files_data = sorted(not_sorted_files_data, key=lambda x: x[3], reverse=True)
        return render(request, 'index/file.html', locals())


def upload(request):
    if request.method == 'POST':
        file_data = request.FILES.get('file')
        if not file_data:
            not_file_message = translate_message('No file has been selected yet, please select a file')
            return render(request, 'index/upload.html', locals())
        error_file_name_length = False
        file_name = str(file_data.name)
        if '.' in file_name and len(file_name.rsplit('.', 1)[0]) < 2:  # 有拓展名文件名长度小于2
            error_file_name_length = True
        if  '.' not in file_name and len(file_name) < 2:  # 无拓展名文件名长度小于2
            error_file_name_length = True
        if error_file_name_length:
            error_file_name_message = translate_message('The length of the file name should not be less than 2. Please select the file again')
            return render(request, 'index/upload.html', locals())
        if file_data.size > 5 * 1024 * 1024:
            error_file_size_message = translate_message('The file size should be less than 5M. Please reselect the file')
            return render(request, 'index/upload.html', locals())
        files_size_dict = File.objects.aggregate(Sum('file_size'))
        if files_size_dict['file_size__sum'] and files_size_dict['file_size__sum'] > 300 * 1024 * 1024:  # 总文件大小超过 300M
            over_files_size_message = translate_message('The file system is running low on memory. Please try again later or contact website management')
            return render(request, 'index/upload.html', locals())
        exist_file = File.objects.filter(file_name=file_name)
        if not exist_file:
            new_file = File.objects.create()
            new_file.file_name = file_name
            new_file.file_size = file_data.size
            new_file.save()
        handle_uploaded_file(file_data, file_name)
        success_upload_message = f'{file_name} '+ translate_message('upload successful, please continue')
        return render(request, 'index/upload.html', locals())
    return render(request, 'index/upload.html', locals())


def handle_uploaded_file(file_data, filename):
    file_upload_path = os.path.join(base_dir, 'files')
    if not os.path.exists(file_upload_path):
        os.makedirs(file_upload_path)
    with open(file_upload_path + '/' + filename, 'wb+') as f:
        for chunk in file_data.chunks():
            f.write(chunk)


def download(request, file_id):
    """
    点击文件名下载, 将此文件下载数加 1, 重定向当前页面刷新数据
    并将文件夹 id 和 name 临时存起来, 真正下载文件
    """
    file = File.objects.get(id=file_id)
    file_name = file.file_name
    file.downloads += 1
    file.save()
    request.session['file_id'] = file_id
    request.session['file_name'] = file_name
    return HttpResponseRedirect(reverse('index:files'))

def download_file(request, file_id):
    """ 实际下载文件 """
    del request.session['file_id']
    del request.session['file_name']
    file = File.objects.get(id=file_id)
    file_name = file.file_name
    file_path = os.path.join(base_dir, 'files', file_name)
    file_data = open(file_path, 'rb')
    response = FileResponse(file_data)
    response['Content-Type'] = 'application/octet-stream'
    # 文件名为中文时无法识别，使用 UTF-8 和 escape_uri_path 处理
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(file_name))
    return response
