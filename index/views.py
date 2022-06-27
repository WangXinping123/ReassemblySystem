from django.shortcuts import render


# Create your views here.
def index_view(request):
    # print("kkkkkkk")
    return render(request, 'index/index.html')


def pointshow_view(request):
    return render(request, 'three-dimensional/pointshow.html')


def pointupload_view(request):
    return render(request, 'three-dimensional/pointupload.html')


def pictureshow_view(request):
    return render(request, 'two-dimensional/pictureshow.html')


def pictureupload_view(request):
    return render(request, 'two-dimensional/pictureupload.html')
