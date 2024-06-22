from django.core.management.base import BaseCommand
from thedatabet.stats import main


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()