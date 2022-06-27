from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/index/index/
    path('index/', views.index_view),
    # http://127.0.0.1:8000/index/pointshow/
    path('pointshow/', views.pointshow_view),
    # http://127.0.0.1:8000/index/pointupload/
    path('pointupload/', views.pointupload_view),
    # http://127.0.0.1:8000/index/pictureshow/
    path('pictureshow/', views.pictureshow_view),
    # http://127.0.0.1:8000/index/pictureupload/
    path('pictureupload/', views.pictureupload_view)
]
