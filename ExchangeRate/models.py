from django.db import models

# Create your models here.


class ExchangeRate(models.Model):
    rate_date = models.DateField(verbose_name='日期')
    usd2cny = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='美元')
    hkd2cny = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='港币')

    class Meta:
        ordering = ['-rate_date']
        verbose_name = verbose_name_plural = "汇率"

    def __str__(self):
        return self.rate_date.strftime("%Y-%m-%d")

