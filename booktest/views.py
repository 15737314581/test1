from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 1.定义视图函数，HttpResponse()
# 2.进行url配置，建立url地址与视图的对应关系
# http://127.0.0.1:8000/index

def index(request):
    # 进行处理 和M和T进行交互
    return HttpResponse("哈哈哈")
