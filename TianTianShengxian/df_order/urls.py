from django.conf.urls import include, url
from df_order import views

urlpatterns = [
    url(r'^$', views.order),
    url(r'^order_handle/$', views.order_handle),
    url(r'pay&(\d+)/$', views.pay),
    url(r'viewlog&(\d+)/$', views.viewlog),
]

