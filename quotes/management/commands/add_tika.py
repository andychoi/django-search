from django.core.management.base import BaseCommand
from faker import Faker
import requests
import tika
from tika import parser as p

from ...models import Quote


class Command(BaseCommand):
    help = "Adds from tika"

    def handle(self, *args, **options):

        """ dict_keys(['metadata', 'content', 'status'])
        """
        def get_data_from_web(url):
            response = requests.get(url)
            results = p.from_buffer(response.content)
            return results

        def get_data_from_file(file_path):
            results = p.from_file(file_path)
            return results

        fake = Faker()

        results = get_data_from_file('quotes/management/commands/sample_60MB.pdf')
        Quote.objects.create(name=fake.name(), quote=results["content"])
        print("Completed!!! record created using tika - sample_60MB.pdf")

        results = get_data_from_file('quotes/management/commands/sample.pdf')
        Quote.objects.create(name=fake.name(), quote=results["content"])
        print("Completed!!! record created using tika - sample.pdf")

        pdf_url = "https://www.bl.uk/learning/resources/pdf/makeanimpact/sw-transcripts.pdf"
        results = get_data_from_web(pdf_url)
        print(results["status"])
        Quote.objects.create(name=fake.name(), quote=results["content"])
        print("Completed!!! record created using tika")
