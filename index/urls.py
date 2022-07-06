from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/index/index/
    path('index/', views.index_view),

    # **************************三维*******************************
    # 3D完整点云操作
    # http://127.0.0.1:8000/index/pointshow/
    path('pointshow/', views.pointshow_view),
        # 完整点云删除
        path('pointdelete/', views.pointdelete),
        # 完整点云展示
        path('pointshow1/', views.pointshow1_view),
        # 完整点云上传操作
        path('point_upload/', views.point_upload),
    # 3D碎片操作
    # http://127.0.0.1:8000/index/pointupload/
    path('pointupload/', views.pointupload_view),
        # 点云碎片删除
        path('point_patch_delete/', views.point_patch_delete),
        # 点云碎片展示
        path('point_patch_show1/', views.point_patch_show1_view),
        # 点云碎片展示
        path('point_patch_upload/', views.point_patch_upload),


    # *************************二维********************************
    # http://127.0.0.1:8000/index/pictureshow/
    path('pictureshow/', views.pictureshow_view),
    # http://127.0.0.1:8000/index/pictureupload/
    path('pictureupload/', views.pictureupload_view)
]
