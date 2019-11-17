from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('api/<str:st>', api, name="api"),
    path('get_resource/<str:loc_id>/<str:cate_id>', get_resource, name="get_resource"),
    path('get_items_cate/', get_items_cate, name="get_items_cate"),
    path('get_statistic_data/<int:year>/<int:month>/<int:day>', get_statistic_data, name="get_statistic_data"),
    path('read/Resource', read_resource, name="read_resource"),
    path('read/<str:st>', read, name='read'),
    path('create/ReceiveRecord', create_receive_record, name='create_receive_record'),
    path('create/SendRecord', create_send_record, name='create_send_record'),
    path('create/<str:st>', create, name='create'),
    path('update/<str:st>/<int:pk>', update, name='update'),
    path('delete/<str:st>/<int:pk>', delete, name='delete'),
    path('detail/<str:st>/<int:pk>', detail, name='detail'),
    path('QRcodeScanner', QRcodeScanner, name='QRcodeScanner'),
]