from django.db import models
from django.utils import timezone

class TariffRate(models.Model):
    country = models.CharField(max_length=100)
    hs_code = models.CharField(max_length=20)
    rate_percent = models.FloatField()
    source = models.CharField(max_length=255)
    date_effective = models.DateField()
    last_updated = models.DateTimeField(default=timezone.now)

class FreightCost(models.Model):
    origin_country = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    container_type = models.CharField(max_length=20)
    cost_usd = models.FloatField()
    source = models.CharField(max_length=255)
    last_updated = models.DateTimeField(default=timezone.now)

class DeliveryCost(models.Model):
    port = models.CharField(max_length=100)
    destination_zip = models.CharField(max_length=10)
    cost_usd = models.FloatField()
    distance_miles = models.FloatField()
    method = models.CharField(max_length=50)
    source = models.CharField(max_length=255)
    last_updated = models.DateTimeField(default=timezone.now)

class ChatBotLog(models.Model):
    user_id = models.CharField(max_length=100)
    message_in = models.TextField()
    message_out = models.TextField(blank=True, null=True)
    track_link = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
