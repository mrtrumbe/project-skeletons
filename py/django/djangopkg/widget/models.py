from django import models

class TradingGroup(models.Model):
    name = models.CharField(max_length=50)
