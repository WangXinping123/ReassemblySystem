from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/user/reg/
    path('reg/', views.reg_view),
    # http://127.0.0.1:8000/user/login1/
    path('login1/', views.login_view)
]
