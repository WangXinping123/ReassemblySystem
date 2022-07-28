from django.db import models
from user.models import User


# Create your models here.
# 完整文物类
class three_pcl_img(models.Model):
    pcl_img = models.FileField(verbose_name="点云", max_length=128, upload_to='3D_point/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

# 碎块类
class three_pcl_img_patch(models.Model):
    pcl_patch = models.FileField(verbose_name="点云", max_length=128, upload_to='3D_patch/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

class two_pcl_img(models.Model):
    pcl_img = models.FileField(verbose_name="二维", max_length=128, upload_to='2D_photo/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)


class two_pcl_img_patch(models.Model):
    pcl_patch = models.FileField(verbose_name="二维", max_length=128, upload_to='2D_patch/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)