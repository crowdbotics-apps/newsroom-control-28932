from rest_framework import serializers
from rundowns.models import Rundown


class RundownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rundown
        fields = "__all__"
