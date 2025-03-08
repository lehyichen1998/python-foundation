from flask import Flask, request, render_template
import requests

app = Flask(__name__, template_folder='../templates')
tomorrow_loacl = r'/tomorrow.html'
moon_loacl = r'/month.html'
week_loacl = r'/week.html'
today_loacl = r'today.html'
url = 'http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f&consName=狮子座&type=today'
##########################################################################Key：212a7e1b3f9c5002dd440372b583bd64

# 那么我们现在知道我么会根据不同的 时间推出 不同的数据 所以我们要根据 用户选择 的类型进行返回
# 当用户输入 今天或者明天跳转套相应的页面

@app.route('/')
def today():
    # global data_time, r
    try:
        r = request.args.get('consName')  # 根据星座
        data_time = request.args.get('datetime')  # 根据时间
        print('consName:', r, 'data_time:', data_time)
        if r is None and data_time is None:  # 当没有参数输入时显示默认
            pass
            result = requests.get('http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f'
                                  '&consName=狮子座&type=today')
            date = result.json()['date']
            name = result.json()['name']
            friend = result.json()['QFriend']
            color = result.json()['color']
            summary = result.json()['summary']
            love = result.json()['love']
            work = result.json()['work']
            print('时间：%s' % date)
            print('星座名称：%s' % name)
            print('切合的星座：%s' % friend)
            print('切合的时间：%s' % color)
            print('要注意的事：%s' % summary)
            print('爱情上：%s' % love)
            print('工作上：%s' % work)
            return render_template(today_loacl, date=date, love=love, name=name, color=color,
                                   summary=summary, work=work, friend=friend)
        elif r != '' and data_time == 'tomorrow':  # 当有参数显示时显示 明天
            result = requests.get('http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f'
                                  '&consName=%s&type=%s' % (r, data_time))
            date = result.json()['date']
            name = result.json()['name']
            friend = result.json()['QFriend']
            color = result.json()['color']
            summary = result.json()['summary']
            love = result.json()['love']
            work = result.json()['work']
            print('时间：%s' % date)
            print('星座名称：%s' % name)
            print('切合的星座：%s' % friend)
            print('切合的时间：%s' % color)
            print('要注意的事：%s' % summary)
            print('爱情上：%s' % love)
            print('工作上：%s' % work)
            return render_template(tomorrow_loacl, date=date, love=love, name=name, color=color,
                                   summary=summary, work=work, friend=friend)
        elif r != '' and data_time == 'today':  # 当有参数显示时  显示今天
            result = requests.get('http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f'
                                  '&consName=%s&type=%s' % (r, data_time))
            date = result.json()['date']
            name = result.json()['name']
            friend = result.json()['QFriend']
            color = result.json()['color']
            summary = result.json()['summary']
            love = result.json()['love']
            work = result.json()['work']
            print('时间：%s' % date)
            print('星座名称：%s' % name)
            print('切合的星座：%s' % friend)
            print('切合的时间：%s' % color)
            print('要注意的事：%s' % summary)
            print('爱情上：%s' % love)
            print('工作上：%s' % work)
            return render_template(today_loacl, date=date, love=love, name=name, color=color,
                                   summary=summary, work=work, friend=friend)
        elif r != '' and data_time == 'weekend':
            data_time = 'week'
            result = requests.get('http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f'
                                  '&consName=%s&type=%s' % (r, data_time))
            result_all = result.json()
            print('用户根据周请求', result_all)
            name = result_all['name']
            print(name)
            date = result_all['date']
            print(date)
            weekth = result_all['weekth']
            health = result_all['health']
            job = result_all['job']
            love = result_all['love']
            money = result_all['money']
            work = result_all['work']
            print('星座名：%s' % name)
            print('请求的时间：%s' % date)
            print('第几个周期：%s' % weekth)
            print('关于健康：%s' % health)
            print('工作预测：%s' % job)
            print('爱情上：%s' % love)
            print('金钱上：%s' % money)
            print('工作上：%s' % work)
            return render_template(week_loacl, name=name, date=date, weekth=weekth, health=health, job=job
                                   , love=love, money=money, work=work)
        elif r != '' and data_time == 'month':
            result = requests.get('http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f'
                                  '&consName=%s&type=%s' % (r, data_time))
            result_all = result.json()
            print('用户根据月请求', result_all)
            name = result_all['name']
            date = result_all['date']
            alls = result_all['all']
            health = result_all['health']
            month = result_all['month']
            love = result_all['love']
            work = result_all['work']
            money = result_all['money']
            print('星座', name)
            print('时间', date)
            print('本月all', alls)
            print('健康', health)
            print('月份', month)
            print('爱情', love)
            print('工作', work)
            print('金钱', money)
            return render_template(moon_loacl, name=name, date=date, alls=alls,
                                   health=health, month=month, love=love, work=work, money=money)
    except Exception as erro:
        print(erro)


if __name__ == '__main__':
    app.run()









