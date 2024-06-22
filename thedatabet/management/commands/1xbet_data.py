from django.core.management.base import BaseCommand
from thedatabet.sportsmole import main


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()