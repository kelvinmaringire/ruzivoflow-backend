from django.core.management.base import BaseCommand
from thedatabet.forebet import main


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()