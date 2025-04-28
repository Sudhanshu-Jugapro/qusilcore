from django.core.management.base import BaseCommand
from ganakdesti.models import TariffRate, FreightCost, DeliveryCost
from datetime import datetime
import random

class Command(BaseCommand):
    help = 'Optimized bulk load of tariffs, freight, and delivery mock data for Qusil2025'

    def handle(self, *args, **kwargs):
        top_producers = [
            "China", "India", "Vietnam", "Indonesia", "Bangladesh", "Turkey", "Pakistan",
            "Mexico", "Brazil", "Philippines", "Thailand", "Ethiopia", "Italy", "Cambodia",
            "Myanmar", "Germany", "Portugal", "Spain", "Tunisia", "Morocco", "Sri Lanka",
            "Malaysia", "Peru", "Egypt", "Romania"
        ]

        skus = [f"SKU-GENTS-{str(i).zfill(3)}" for i in range(1, 21)]

        self.stdout.write('Generating mock tariffs...')
        tariff_objs = []
        for country in top_producers:
            for sku in skus:
                tariff_objs.append(TariffRate(
                    country=country,
                    hs_code="6403.51",
                    rate_percent=round(random.uniform(5, 150), 2),
                    source="Mock-Generated-Policy",
                    date_effective=datetime(2025, 1, 1).date(),
                    last_updated=datetime.now()
                ))
        TariffRate.objects.bulk_create(tariff_objs, batch_size=500)
        self.stdout.write(f'Inserted {len(tariff_objs)} TariffRate records.')

        self.stdout.write('Generating mock freight costs...')
        freight_objs = []
        for country in top_producers:
            freight_objs.append(FreightCost(
                origin_country=country,
                port=f"{country}_Port",
                container_type="20ft",
                cost_usd=round(random.uniform(1800, 6000), 2),
                source="Mock-Generated-Shipping",
                last_updated=datetime.now()
            ))
        FreightCost.objects.bulk_create(freight_objs, batch_size=500)
        self.stdout.write(f'Inserted {len(freight_objs)} FreightCost records.')

        self.stdout.write('Generating mock delivery costs...')
        delivery_objs = []
        for country in top_producers:
            delivery_objs.append(DeliveryCost(
                port=f"{country}_Port",
                destination_zip="90210",
                cost_usd=round(random.uniform(500, 2000), 2),
                distance_miles=round(random.uniform(50, 2500), 1),
                method=random.choice(["truckload", "rail", "mixed"]),
                source="Mock-Generated-Logistics",
                last_updated=datetime.now()
            ))
        DeliveryCost.objects.bulk_create(delivery_objs, batch_size=500)
        self.stdout.write(f'Inserted {len(delivery_objs)} DeliveryCost records.')

        self.stdout.write(self.style.SUCCESS('✅ Optimized mock data loading complete.'))
