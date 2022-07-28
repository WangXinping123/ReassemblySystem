import os
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from user.models import User
from index.models import three_pcl_img, two_pcl_img
from index.models import three_pcl_img_patch, two_pcl_img_patch
from django import forms
from django.core import serializers
from django.conf import settings
import datetime


# Create your views here.
def index_view(request):
    # print("kkkkkkk")
    # print(request.session.get('username'))
    return render(request, 'index/index.html')


# ************************** 3D操作 *******************************
# 3D成品操作
# 1.成品显示操作
def pointshow_view(request):
    queryset = three_pcl_img.objects.filter(user=request.session['userid'])
    return render(request, 'three-dimensional/pointshow.html', {'queryset': queryset})


# 2.成品删除操作
def pointdelete(request):
    pcl_id = request.GET.get('pcl_id')
    three_pcl_img.objects.filter(id=pcl_id).delete()
    return HttpResponseRedirect('/index/pointshow/')


# 3.成品查看操作
def pointshow1_view(request):
    nid = request.GET.get('pcl_id')
    pcl_path1 = three_pcl_img.objects.filter(id=nid).first().pcl_img
    pcl_path = str(pcl_path1)
    pcl_path = os.path.join("../", "../", "../", pcl_path)
    print(pcl_path)
    return render(request, 'three-dimensional/pointlook.html', {"pcl_path": pcl_path})


# 4.上传成品操作
def point_upload(request):
    if request.method == "GET":
        return render(request, 'three-dimensional/pointshow.html')
    # 点云文件筛选
    elif request.method == "POST" and 'button1' in request.POST:
        print(request.POST)
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        queryset = three_pcl_img.objects.filter(user=request.session['userid'],
                                                created_time__range=(data1, data2))
        print(data1)
        print(queryset)
        return render(request, 'three-dimensional/pointshow.html', {'queryset': queryset})
    # 点云文件上传
    elif request.method == "POST" and 'point' in request.POST:
        if request.FILES.get("pcl-upload") is None:
            queryset = three_pcl_img.objects.filter(user=request.session['userid'])
            return render(request, 'three-dimensional/pointshow.html', {'queryset': queryset})
        pcl_object = request.FILES.get("pcl-upload")
        media_path = os.path.join("media", "3D_point", pcl_object.name)
        f = open(media_path, mode='wb')
        for chunk in pcl_object.chunks():
            f.write(chunk)
        f.close()
        user = User.objects.filter(userid=request.session['userid']).first()
        three_pcl_img.objects.create(
            pcl_img=media_path,
            user=user
        )
        queryset = three_pcl_img.objects.filter(user=request.session['userid'])
        return render(request, 'three-dimensional/pointshow.html', {'queryset': queryset})
    # 批量点云上传
    elif request.method == "POST" and 'lotpoint' in request.POST:
        print("kdakdak")
        print(request.FILES.getlist("pcl-upload"))
        if request.FILES.getlist("pcl-upload") is None:
            queryset = three_pcl_img_patch.objects.filter(user=request.session['userid'])
            return render(request, 'three-dimensional/pointshow.html', {'queryset': queryset})
        pcl_object = request.FILES.getlist("pcl-upload")
        for files in pcl_object:
            media_path = os.path.join("media", "3D_patch", files.name)
            f = open(media_path, mode='wb')
            for chunk in files.chunks():
                f.write(chunk)
            f.close()
            user = User.objects.filter(userid=request.session['userid']).first()
            three_pcl_img.objects.create(
                pcl_img=media_path,
                user=user
            )
        queryset = three_pcl_img.objects.filter(user=request.session['userid'])
        print("11111")
        print(queryset)
        return render(request, 'three-dimensional/pointshow.html', {'queryset': queryset})


# 碎片操作
# 1.碎片展示
def pointupload_view(request):
    queryset = three_pcl_img_patch.objects.filter(user=request.session['userid'])
    return render(request, 'three-dimensional/pointupload.html', {'queryset': queryset})


# 2.删除操作
def point_patch_delete(request):
    pcl_id = request.GET.get('pcl_id')
    three_pcl_img_patch.objects.filter(id=pcl_id).delete()
    return HttpResponseRedirect('/index/pointupload/')


# 3.查看操作
def point_patch_show1_view(request):
    nid = request.GET.get('pcl_id')
    pcl_path1 = three_pcl_img_patch.objects.filter(id=nid).first().pcl_patch
    pcl_path = str(pcl_path1)
    pcl_path = os.path.join("../", "../", "../", pcl_path)
    print(pcl_path)
    return render(request, 'three-dimensional/pointpatch.html', {"pcl_path": pcl_path})


# 4.上传碎片操作
def point_patch_upload(request):
    if request.method == "GET":
        return render(request, 'three-dimensional/pointupload.html')
    # 点云文件筛选
    elif request.method == "POST" and 'button1' in request.POST:
        print(request.POST)
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        queryset = three_pcl_img_patch.objects.filter(user=request.session['userid'],
                                                      created_time__range=(data1, data2))
        return render(request, 'three-dimensional/pointupload.html', {'queryset': queryset})
    # 点云文件上传
    elif request.method == "POST" and 'point' in request.POST:
        print(request.FILES.get("pcl-upload"))
        if request.FILES.get("pcl-upload") is None:
            queryset = three_pcl_img_patch.objects.filter(user=request.session['userid'])
            return render(request, 'three-dimensional/pointupload.html', {'queryset': queryset})
        pcl_object = request.FILES.get("pcl-upload")
        media_path = os.path.join("media", "3D_patch", pcl_object.name)
        f = open(media_path, mode='wb')
        for chunk in pcl_object.chunks():
            f.write(chunk)
        f.close()
        user = User.objects.filter(userid=request.session['userid']).first()
        three_pcl_img_patch.objects.create(
            pcl_patch=media_path,
            user=user
        )
        queryset = three_pcl_img_patch.objects.filter(user=request.session['userid'])
        return render(request, 'three-dimensional/pointupload.html', {'queryset': queryset})
    # 批量点云文件上传
    elif request.method == "POST" and 'lotpoint' in request.POST:
        print(request.FILES.getlist("pcl-upload"))
        if request.FILES.getlist("pcl-upload") is None:
            queryset = three_pcl_img_patch.objects.filter(user=request.session['userid'])
            return render(request, 'three-dimensional/pointupload.html', {'queryset': queryset})
        pcl_object = request.FILES.getlist("pcl-upload")
        for files in pcl_object:
            media_path = os.path.join("media", "3D_patch", files.name)
            f = open(media_path, mode='wb')
            for chunk in files.chunks():
                f.write(chunk)
            f.close()
            user = User.objects.filter(userid=request.session['userid']).first()
            three_pcl_img_patch.objects.create(
                pcl_patch=media_path,
                user=user
            )
        queryset = three_pcl_img_patch.objects.filter(user=request.session['userid'])
        return render(request, 'three-dimensional/pointupload.html', {'queryset': queryset})


# ************************** 2D操作 *******************************
# 碎片操作
# def pictureshow_view(request):
#     return render(request, 'two-dimensional/pictureshow.html')


# 1.碎片展示
def pictureupload_view(request):
    queryset = two_pcl_img_patch.objects.filter(user=request.session['userid'])
    return render(request, 'two-dimensional/pictureupload.html', {'queryset': queryset})


# 2.删除操作
def picture_patch_delete(request):
    pcl_id = request.GET.get('pcl_id')
    two_pcl_img_patch.objects.filter(id=pcl_id).delete()
    return HttpResponseRedirect('/index/pointupload/')


# 3.查看操作
def picture_patch_show1_view(request):
    nid = request.GET.get('pcl_id')
    pcl_path1 = three_pcl_img_patch.objects.filter(id=nid).first().pcl_patch
    pcl_path = str(pcl_path1)
    pcl_path = os.path.join("../", "../", "../", pcl_path)
    print(pcl_path)
    return render(request, 'two-dimensional/picturepatch.html', {"pcl_path": pcl_path})


# 4.上传碎片操作
def picture_patch_upload(request):
    if request.method == "GET":
        return render(request, 'two-dimensional/pictureupload.html')
    print(request.FILES)
    pcl_object = request.FILES.get("pcl-upload")
    media_path = os.path.join("media", "2D_patch", pcl_object.name)
    f = open(media_path, mode='wb')
    for chunk in pcl_object.chunks():
        f.write(chunk)
    f.close()
    user = User.objects.filter(userid=request.session['userid']).first()
    two_pcl_img_patch.objects.create(
        pcl_patch=media_path,
        user=user
    )
    queryset = two_pcl_img_patch.objects.filter(user=request.session['userid'])
    return render(request, 'two-dimensional/pictureupload.html', {'queryset': queryset})


# 2D成品操作
# 1.成品显示操作
def pictureshow_view(request):
    queryset = two_pcl_img.objects.filter(user=request.session['userid'])
    return render(request, 'two-dimensional/pictureshow.html', {'queryset': queryset})


# 2.成品删除操作
def picturedelete(request):
    pcl_id = request.GET.get('pcl_id')
    two_pcl_img.objects.filter(id=pcl_id).delete()
    return HttpResponseRedirect('/index/pointshow/')


# 3.成品查看操作
def pictureshow1_view(request):
    nid = request.GET.get('pcl_id')
    pcl_path1 = two_pcl_img.objects.filter(id=nid).first().pcl_img
    pcl_path = str(pcl_path1)
    pcl_path = os.path.join("../", "../", "../", pcl_path)
    print(pcl_path)
    return render(request, 'two-dimensional/picturelook.html', {"pcl_path": pcl_path})


# 4.上传成品操作
def picture_upload(request):
    if request.method == "GET":
        return render(request, 'two-dimensional/pictureshow.html')
    print(request.FILES)
    pcl_object = request.FILES.get("pcl-upload")
    media_path = os.path.join("media", "2D_photo", pcl_object.name)
    f = open(media_path, mode='wb')
    for chunk in pcl_object.chunks():
        f.write(chunk)
    f.close()
    user = User.objects.filter(userid=request.session['userid']).first()
    three_pcl_img.objects.create(
        pcl_img=media_path,
        user=user
    )
    queryset = two_pcl_img.objects.filter(user=request.session['userid'])
    return render(request, 'two-dimensional/pictureshow.html', {'queryset': queryset})
