from rest_framework import serializers

from .models import BettingTips, BettingStats, BetwayOdds


class BettingTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingTips
        fields = '__all__'


class BettingStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingStats
        fields = '__all__'


class BetwayOddsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetwayOdds
        fields = '__all__'

