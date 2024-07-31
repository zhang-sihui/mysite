# Brief introduction

A personal website by Django.

## Development environment

- Windows 11
- Python 3.11.5
- Django 4.2.7

## Preparation for runserver

- 安装模块：
  - 按照 requirements.txt 文件安装需要的模块，可以单个 `pip install xxx`；也可以一次全部安装，不过需要在项目文件夹路径下执行 `pip install -r requirements.txt`。
- 初始化数据库：
  - 在项目路径下，执行两条命令即可初始化数据库：`python manage.py makemigrations`，`python manage.py migrate`。
- 创建超级用户：
  - 在项目路径下：输入 `python manage.py createsuperuser`，进入超级用户（即管理员）创建终端。
  - 依次提示输入用户名，邮箱（可为空），密码，验证密码，即可成功创建。

## Runserver

- 终端下，进入 mysite 项目文件夹。
- 输入以下命令，回车运行启动服务：`python manage.py runserver`。

## Browser search

- User UI(用户)：<http://127.0.0.1:8000>
- Admin UI(管理)：<http://127.0.0.1:8000/admin>

## History

v1.0.5

- 将「文章」页内的「标签」按字母顺序排列，「年份」倒序排序。
- 修复「评论」页内评论列表中评论与回复时间一样的问题。

v1.0.4

- 新建 Author，Category，Status 表，在 admin 后台将新建文章时的这几个字段由输入改为下拉选择。

v1.0.3

- 文章页点击标签或年份或内容时，无法回到文章首页，添加回到全部文章按钮。
- 文章的内容代码块没有分割线，表格没有分割线，添加缺失的 css 样式。
- 新增全局回到顶部功能。

v1.0.2

- 下载文件的列表顺序由无序修改为上传时间倒序排列。
- 上传文件成功后的消息加上文件名。
- 删除留言后给管理员发送邮件的功能。
- 将 jQuery、font-awesome、bootstrap 的在线 CDN 资源修改为本地资源。

v1.0.1

- 文件系统功能：上传、下载文件，文件下载量统计功能。

v1.0.0

- 博客功能：博客发布、编辑、分类、浏览量统计功能。
- 留言功能：支持留言、管理员回复、邮件通知功能网站管理员。
