from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib


# Create your views here.
# 注册
def reg_view(request):
    # Get，返回页面
    if request.method == 'GET':
        return render(request, 'user/register1.html')
    # Post 处理提交数据
    elif request.method == 'POST':
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        # 1，两个密码要保持一致
        if password_1 != password_2:
            return HttpResponse('两次密码输入不一致')
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()
        # 2，当前用户名是否可用
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户名已注册')
        # 3，插入数据
        try:
            User.objects.create(username=username, password=password_m)
        except Exception as e:
            print('--create user error %s' % (e))
            return HttpResponse('用户名已注册')
        # print("kkkkkkkkkkksssssss")
        return HttpResponseRedirect('/user/login1/')


def login_view(request):
    if request.method == 'GET':
        # 获取登录页面
        # 检查登录状态，如果登录了，显示‘已登录’
        # if request.session.get('username') and request.session.get('uid'):
        #     return HttpResponseRedirect('/index/index/')
        # c_username = request.COOKIES.get('username')
        # c_uid = request.COOKIES.get('uid')
        # if c_username and c_uid:
        #     # 回写session
        #     request.session['username'] = c_username
        #     request.session['uid'] = c_uid
        #     return HttpResponseRedirect('/index/index/')
        return render(request, 'user/login1.html')
    elif request.method == 'POST':
        # 处理数据
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        print(username)
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s' % (e))
            return HttpResponse('用户名或密码错误')
        # 对比密码
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('用户名或密码错误')
        request.session['username'] = username
        request.session['uid'] = user.id
        resp = HttpResponseRedirect('/index/index/')
        # # 判断用户是否点选了‘用户名’
        # if 'remember' in request.POST:
        #     resp.set_cookie('username', username, 3600 * 24 * 3)
        #     resp.set_cookie('uid', user.id, 3600 * 24 * 3)
        return resp
