from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def hello():
    return 'hello-你好啊!'

@my_app.route('/news')
def news():
    return '<h1>欢迎来到新闻页面~</h1>'

@my_app.route('/maps')
def maps():
    return '<h1>欢迎来到地图页面~</h1>'
my_app.run()


