from rest_framework import serializers

from .models import BettingTips

class BettingTipsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BettingTips
        fields = '__all__'

