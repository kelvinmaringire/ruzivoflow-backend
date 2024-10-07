from django.core.management.base import BaseCommand
from thedatabet.onexbet import main
import asyncio


class Command(BaseCommand):
    def handle(self, *args, **options):
        asyncio.run(main())