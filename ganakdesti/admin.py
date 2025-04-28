from django.contrib import admin
from .models import TariffRate, FreightCost, DeliveryCost, ChatBotLog

admin.site.register(TariffRate)
admin.site.register(FreightCost)
admin.site.register(DeliveryCost)
admin.site.register(ChatBotLog)
