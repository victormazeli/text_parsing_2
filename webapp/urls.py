from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('insert', insert, name='insert'),
    path('records', records, name='records'),
    path('delete_topic', delete_topic, name='delete_topic'),
    path('next', next, name='next'),
    path('prev', prev, name='prev'),
    path('add', add, name='add'),
    path('delete_records', delete_records, name='delete_records'),
    path('clear_records', clear_records, name='clear_records'),
    path('download', download, name='download'),
    path('detect_on', detect_on, name='detect_on'),
    path('detect_off', detect_off, name='detect_off'),
    path('download', download, name='download'),

]
