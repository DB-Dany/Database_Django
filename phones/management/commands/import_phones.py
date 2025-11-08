import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_path = options['csv_file']
        with open(csv_path, 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # Создаем slug из имени
            slug = slugify(phone['name'])

            Phone.objects.update_or_create(
                id=int(phone['id']),
                defaults={
                    'name': phone['name'],
                    'price': float(phone['price']),
                    'image': phone['image'],
                    'release_date': datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
                    'lte_exists': phone['lte_exists'].lower() == 'true',
                    'slug': slug,  # Явно устанавливаем slug
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))