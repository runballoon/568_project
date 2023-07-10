from django.db import models

class Stocks(models.Model):
    company = models.CharField(max_length=128, default="")
    ticker = models.CharField(max_length=128)
    current = models.FloatField(null=True, blank=True, default=None)
    one_pred = models.FloatField(null=True, blank=True, default=None)
    one_pred_diff = models.FloatField(null=True, blank=True, default=None)
    three_pred = models.FloatField(null=True, blank=True, default=None)
    three_pred_diff = models.FloatField(null=True, blank=True, default=None)
    seven_pred = models.FloatField(null=True, blank=True, default=None)
    seven_pred_diff = models.FloatField(null=True, blank=True, default=None)
    update_time = models.DateField(null=True, blank=True, default=None)

class Overviews(models.Model):
    company = models.CharField(max_length=128, default="")
    ticker = models.CharField(max_length=128)
    date = models.DateField(null=True, blank=True, default=None)
    open = models.FloatField(null=True, blank=True, default=None)
    high = models.FloatField(null=True, blank=True, default=None)
    low = models.FloatField(null=True, blank=True, default=None)
    close = models.FloatField(null=True, blank=True, default=None)
    adjclose = models.FloatField(null=True, blank=True, default=None)
    volume = models.IntegerField(null=True, blank=True, default=None)