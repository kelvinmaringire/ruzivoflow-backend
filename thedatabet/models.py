from django.db import models


class BettingTips(models.Model):
    date = models.DateField()
    games = models.JSONField()
    host_sc_mse = models.FloatField()
    host_sc_r2 = models.FloatField()
    guest_sc_mse = models.FloatField()
    guest_sc_r2 = models.FloatField()
    result_mse = models.FloatField()
    result_r2 = models.FloatField()