from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import View


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello, World!')

