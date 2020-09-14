from django.conf.urls import include,url
from df_goods import views

# df_goods模块下对应的url
urlpatterns = [
    url(r'^$', views.index), # 首页
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.good_list, name="list"),
    url(r'^(\d+)/$', views.detail),
]
