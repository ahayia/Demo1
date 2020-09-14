# coding:utf-8
"""
此函数为装饰器，用来验证用户是否登录，并返回到对应的请求页面
当请求 http://127.0.0.1:8000/200/?type=10
request.path:表示当前路径，/200/
request.get_full_path(),:表示完整路径，/200/?type=10
"""
from django.http import HttpResponseRedirect


def login(func):
    def login_fun(request, *args, **kwargs):

        if request.session.has_key('user_id'):
            # 如果登陆成功继续执行原函数
            return func(request, *args, **kwargs)
        else:
            print('请登录')
            red = HttpResponseRedirect('/user/login/') # 没有登陆就跳转到登陆界面
            red.set_cookie('url', request.get_full_path()) # 获取当前url路径存入cookie
            return red
    return login_fun
