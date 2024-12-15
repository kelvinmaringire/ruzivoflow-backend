import asyncio
from django.core.management.base import BaseCommand
from thedatabet.betway_copy import main


class Command(BaseCommand):
    help = "Fetch and save Betway odds."

    def handle(self, *args, **options):
        asyncio.run(main())
