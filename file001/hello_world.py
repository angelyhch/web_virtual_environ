'''
set FLASK_APP=【程序名称】
flask run        #启动flask程序，程序必须存放在当前命令执行路径下；

flask run 【--port】 #可以指定端口号，默认是5000，指定后可以更改；

开发环境（development enviroment）和生产环境（production
enviroment）是我们后面会频繁接触到的概念。开发环境是指我们在本地编写和测
试程序时的计算机环境，而生产环境与开发环境相对，它指的是网站部署上线供用
户访问时的服务器环境。
根据运行环境的不同，Flask程序、扩展以及其他程序会改变相应的行为和设
置。为了区分程序运行环境，Flask提供了一个FLASK_ENV环境变量用来设置环境，
默认为production（生产）。在开发时，我们可以将其设为development（开
发），这会开启所有支持开发的特性。为了方便管理，我们将把环境变量
FLASK_ENV的值写入.flaskenv文件中：
FLASK_ENV=development
现在启动程序，你会看到下面的输出提示：
$ flask run
* Environment: development
* Debug mode: on
* Debugger is active!
* Debugger PIN: 202-005-064
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
在开发环境下，调试模式（Debug Mode）将被开启，这时执行flask run启动
程序会自动激活Werkzeug内置的调试器（debugger）和重载器（reloader），它
们会为开发带来很大的帮助
'''

'''
1.6项目配置
配置的名称必须是全大写形式，小写的变量将不会被读取。
使用update（）方法则可以一次加载多个值：
app.config.update(
TESTING=True,
SECRET_KEY='_5#yF4Q8z\n\xec]/'）



'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

print(app.name)

if __name__ == '__main__':
    app.run()