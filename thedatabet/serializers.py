from rest_framework import serializers

from .models import BettingTips

class BettingTipsSerializer(serializers.ModelSerializer):
    doc_url = serializers.SerializerMethodField('get_doc_url')

    class Meta:
        model = BettingTips
        fields = '__all__'

    def get_doc_url(self, obj):
        if obj.tips:
            request = self.context.get('request')
            doc_url = obj.tips.file.url
            return request.build_absolute_uri(doc_url)
        return None

