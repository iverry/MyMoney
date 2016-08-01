from django.db import models
from enum import Enum
# Create your models here.

CurrenyUseType = Enum('CurrenyUseType', '投资 自用')

class BAccount(models.Model):
    name = models.CharField(max_length=40, verbose_name='账户名称')
    currency = models.CharField(max_length=3, verbose_name='币种', default='CNY')

