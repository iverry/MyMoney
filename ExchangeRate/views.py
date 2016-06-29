from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import ExchangeRate


class IndexView(generic.ListView):
    template_name = 'ExchangeRate/index.html'
    context_object_name = 'latest_rate_list'

    def get_queryset(self):
        return ExchangeRate.objects.order_by('-rate_date')[:5]

