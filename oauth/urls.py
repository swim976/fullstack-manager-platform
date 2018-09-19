from django.urls import path

from . import views

app_name = "oauth"
urlpatterns = [
    # url(r'^login$', views.login),      # 获取token
    # url(r'^get_token_info$', views.getTokenInfo),   # 获取信息查询接口
    # url(r'^revokeoauth$', views.revokeOauth),       # 授权回收接口
    path("weblogin", views.weblogin, name="weblogin")
]
