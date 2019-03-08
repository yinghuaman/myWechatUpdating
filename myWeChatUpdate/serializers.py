from rest_framework import serializers
from .models import WechatUpdate

class WechatUpdateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = WechatUpdate
        fields = ["id","text","image","create_time","username"]

