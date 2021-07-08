# coding = utf-8
from django.conf.urls import url
from booktest import views



urlpatterns = [
    # 通过url函数设置url配置项
    url('^index$',views.index) # 建立/index与视图index直接的关系

]