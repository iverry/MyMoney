#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-20 15:59:54
# @Author  : 'lianjinxiang01'
# @Link    : http://example.org
# @Version : $


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='main-view'),
]