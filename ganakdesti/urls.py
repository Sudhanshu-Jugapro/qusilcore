from django.urls import path
from .views import (
    TariffRateList, FreightCostList,
    DeliveryCostList, ChatBotLogCreate
)
from .views import dashboard

urlpatterns = [
    path('api/tariffs/', TariffRateList.as_view()),
    path('api/freight-costs/', FreightCostList.as_view()),
    path('api/delivery-costs/', DeliveryCostList.as_view()),
    path('api/rebid-log/', ChatBotLogCreate.as_view()),
    path('dashboard/', dashboard, name='dashboard'),
]
