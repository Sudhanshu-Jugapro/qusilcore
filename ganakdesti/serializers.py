from rest_framework import serializers
from .models import TariffRate, FreightCost, DeliveryCost, ChatBotLog

class TariffRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffRate
        fields = '__all__'

class FreightCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreightCost
        fields = '__all__'

class DeliveryCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = '__all__'

class ChatBotLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBotLog
        fields = '__all__'
