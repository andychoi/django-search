from django.core.management.base import BaseCommand
from faker import Faker
import requests
import tika
from tika import parser as p

from ...models import Content

# https://medium.com/mlearning-ai/convert-any-type-of-document-to-text-with-apache-tika-using-python-api-ff306c467b3

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

        results = get_data_from_file('contents/management/commands/sample_form.pdf')
        Content.objects.create(title=fake.name(), content=results["content"])
        print("Completed!!! record created using tika - sample_form.pdf")

        results = get_data_from_file('contents/management/commands/sample.pdf')
        Content.objects.create(title=fake.name(), content=results["content"])
        print("Completed!!! record created using tika - sample.pdf")

        pdf_url = "https://www.irs.gov/pub/irs-pdf/p515.pdf"
        results = get_data_from_web(pdf_url)
        Content.objects.create(title=fake.name(), content=results["content"])
        print("Completed!!! record created using tika - IRS web p515.pdf")

        pdf_url = "https://www.bl.uk/learning/resources/pdf/makeanimpact/sw-transcripts.pdf"
        results = get_data_from_web(pdf_url)
        print(results["status"])
        Content.objects.create(title=fake.name(), content=results["content"])
        print("Completed!!! record created using tika")
