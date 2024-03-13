from rest_framework import serializers
from . models import person

class personserializer(serializers.ModelSerializer):
    class Meta:
        models=person
        fields=['Name','Age','Contact','Gender']