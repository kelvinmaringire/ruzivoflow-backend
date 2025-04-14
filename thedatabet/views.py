from rest_framework import generics

from .models import BettingTips
from .serializers import BettingTipsSerializer


class BettingTipsList(generics.ListAPIView):
    queryset = BettingTips.objects.all()
    serializer_class = BettingTipsSerializer
