from django.http import HttpResponse

from rest_framework import generics

from .scripts import main
from .models import BettingTips
from .serializers import BettingTipsSerializer


class BettingTipsList(generics.ListAPIView):
    queryset = BettingTips.objects.all()
    serializer_class = BettingTipsSerializer


def run_main_script(request):
    main()
    return HttpResponse("Script ran successfully!")