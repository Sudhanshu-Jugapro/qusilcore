from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework import generics
from .models import TariffRate, FreightCost, DeliveryCost, ChatBotLog
from .serializers import (
    TariffRateSerializer, FreightCostSerializer,
    DeliveryCostSerializer, ChatBotLogSerializer
)

class TariffRateList(generics.ListAPIView):
    serializer_class = TariffRateSerializer
    def get_queryset(self):
        return TariffRate.objects.filter(
            country=self.request.GET.get('country'),
            hs_code=self.request.GET.get('hs_code')
        )

class FreightCostList(generics.ListAPIView):
    serializer_class = FreightCostSerializer
    def get_queryset(self):
        return FreightCost.objects.filter(
            origin_country=self.request.GET.get('origin_country'),
            container_type=self.request.GET.get('container_type')
        )

class DeliveryCostList(generics.ListAPIView):
    serializer_class = DeliveryCostSerializer
    def get_queryset(self):
        return DeliveryCost.objects.filter(
            port=self.request.GET.get('port'),
            destination_zip=self.request.GET.get('destination_zip')
        )

class ChatBotLogCreate(generics.CreateAPIView):
    queryset = ChatBotLog.objects.all()
    serializer_class = ChatBotLogSerializer

def dashboard(request):
    # Filters
    tariff_country = request.GET.get('tariff_country')
    freight_origin = request.GET.get('freight_origin')
    freight_port = request.GET.get('freight_port')

    tariffs = TariffRate.objects.all()
    if tariff_country:
        tariffs = tariffs.filter(country=tariff_country)

    freights = FreightCost.objects.all()
    if freight_origin:
        freights = freights.filter(origin_country=freight_origin)
    if freight_port:
        freights = freights.filter(port=freight_port)

    deliveries = DeliveryCost.objects.all()

    # Pagination setup
    tariff_paginator = Paginator(tariffs, 10)  # 10 records per page
    freight_paginator = Paginator(freights, 10)
    delivery_paginator = Paginator(deliveries, 10)

    page1 = request.GET.get('page1')
    page2 = request.GET.get('page2')
    page3 = request.GET.get('page3')

    tariff_page = tariff_paginator.get_page(page1)
    freight_page = freight_paginator.get_page(page2)
    delivery_page = delivery_paginator.get_page(page3)

    # Dropdown filter values
    tariff_countries = TariffRate.objects.values_list('country', flat=True).distinct().order_by('country')
    freight_origins = FreightCost.objects.values_list('origin_country', flat=True).distinct().order_by('origin_country')
    freight_ports = FreightCost.objects.values_list('port', flat=True).distinct().order_by('port')

    return render(request, 'ganakdesti/dashboard.html', {
        'tariff_page': tariff_page,
        'freight_page': freight_page,
        'delivery_page': delivery_page,
        'tariff_countries': tariff_countries,
        'freight_origins': freight_origins,
        'freight_ports': freight_ports,
        'selected_tariff': tariff_country,
        'selected_origin': freight_origin,
        'selected_port': freight_port,
    })