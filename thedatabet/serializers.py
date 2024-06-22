from rest_framework import serializers

from .models import BettingTips, BettingStats


class BettingTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingTips
        fields = '__all__'


class BettingStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingStats
        fields = '__all__'

