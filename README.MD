# Swaggerdoc

## 说明
这是一个简便的django app将swagger ui搬到项目中展示。开发人员只需将swagger文档放到项目指定目录，即可打开相应的URL查看swagger文档，非常适合使用Django开发的项目，在开发过程同时编写文档，并同步更新到项目中，团队其他人员也可以同时看到最新修改的文档。

## 用法

Django APP为`swaggerdoc`，像其他APP一样将该目录放到项目目录中。然后准备一些配置：

1. 在项目setting中的INSTALLED_APPS列表写入'swaggerdoc', 主要便于Django自动查找'swaggerdoc'APP中的static和templates目录下面的文件。该APP没有models文件，如果不想写入INSTALLD_APPS，需要将静态文件目录包含swaggerdoc内的`static`和`templates`目录。
2. 在项目setting中设置`DOC_DIR`, 存放swagger文档的目录。也可以不设置，默认为项目目录下的`docs`文件夹。
3. 设置`STATICFIELS_DIRS`，包含第2点的`DOC_DIR`。如设置为`os.path.join(BASE_DIR, 'docs')`，使得Django可以找到该目录下的swagger文档。
4. 设置`url patterns`, 在项目的`urls.py`文件设置swagger文档访问路径，包含`swaggerdoc.urls`即可。如: `url(r'^api/doc/', include('swaggerdoc.urls')`。

这样，启动项目服务器，即可打开浏览器访问`{服务其地址}/api/doc`就可以看到项目文档了。

效果图如下：

![](http://7xpcbe.com1.z0.glb.clouddn.com/%E6%88%AA%E5%9B%BE_2017-03-22_10-21-52.png)

代码是一个完整的django工程，提供可运行的示例, 直接git clone试运行。
