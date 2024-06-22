from django.http import HttpResponse

from rest_framework import generics

from .forebet import main
from .models import BettingTips, BettingStats
from .serializers import BettingTipsSerializer, BettingStatsSerializer


class BettingTipsList(generics.ListAPIView):
    queryset = BettingTips.objects.all()
    serializer_class = BettingTipsSerializer
    

class BettingStatsList(generics.ListAPIView):
    queryset = BettingStats.objects.all()
    serializer_class = BettingStatsSerializer


def run_main_script(request):
    main()
    return HttpResponse("Script ran successfully!")