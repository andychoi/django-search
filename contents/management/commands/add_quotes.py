from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Content


class Command(BaseCommand):
    help = "Adds contents to the database"

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(10000):
            Content.objects.create(title=fake.name(), content=fake.text())

        print("Completed!!! Check your database.")
