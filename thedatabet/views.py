from rest_framework import generics

from .models import BettingTips, BettingStats, BetwayOdds
from .serializers import BettingTipsSerializer, BettingStatsSerializer, BetwayOddsSerializer


class BettingTipsList(generics.ListAPIView):
    queryset = BettingTips.objects.all()
    serializer_class = BettingTipsSerializer
    

class BettingStatsList(generics.ListAPIView):
    queryset = BettingStats.objects.all()
    serializer_class = BettingStatsSerializer


class BetwayOddsList(generics.ListAPIView):
    queryset = BetwayOdds.objects.all()
    serializer_class = BetwayOddsSerializer
