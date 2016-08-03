# 功能说明
php代码风格检查工具,在接收到 github pull request 相关事件的时候，使用 php-cs-fixer 来进行代码风格检查。
# 安装使用
在一台可以联网的服务器上执行下列命令

    git clone git@gitlab.baixing.cn:jswh/Zeus.git
    cd Zeus
    sudo python server.py

如果出现依赖错误，请根据说明用 pip 安装相关依赖。
# github 配置
在 repo 界面选择Settings > Webhooks & services, 点击Add Webhooks

参数如下

* Payload Url: http://{domain}/api/webhook
* Content type: application/json
* Secret 留空即可
* Send me everything
* 勾选Active

# Tips
* 服务器上的git必须要有相关repo的操作权限才可以正常工作
* 代码风格的调整有两个方式
    * 直接更换php-cs-fixer.phar，可以使用[这个带有打包脚本的repo](https://github.com/jswh/PHP-CS-Fixer)
    * 修改 pipeline/tasks/check_style.py 中的相关命令, [命令参数列表](https://github.com/FriendsOfPHP/PHP-CS-Fixer/blob/1.11/README.rst)
