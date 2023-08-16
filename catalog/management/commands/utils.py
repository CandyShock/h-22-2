import json

from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = [
            {
                "nomination": "Часы",
                "description": "показывают время",
                "image": "",
                "category": "time",
                "price": 20,
                "date": "2023-07-04T06:00:00Z",
                "last_modified_date": "2023-07-12T12:00:00Z"
            },
            {
                "nomination": "Весы",
                "description": "показывают вес",
                "image": "",
                "category": "time",
                "price": 20,
                "date": "2023-07-04T06:00:00Z",
                "last_modified_date": "2023-07-12T12:00:00Z"
            }
        ]
        data_2 = [
            {
                "nomination": "Phone",
                "description": "tools"
            },
            {
                "nomination": "Name",
                "description": "Name"
            }
        ]
        records = Product.objects.all()
        records.delete()
        records_ = Category.objects.all()
        records_.delete()

        Product_for_create = []
        Category_for_create = []

        for item_product in data:
            Product_for_create.append(Product(**item_product))

        for item_category in data_2:
            Category_for_create.append(Category(**item_category))

        Product.objects.bulk_create(Product_for_create)
        Category.objects.bulk_create(Category_for_create)
