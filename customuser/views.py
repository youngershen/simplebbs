# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

from django.shortcuts import render
from django.http import HttpResponse

def index(request, *args, **kwargs):
    return HttpResponse('test')
