# core/serializers.py
from rest_framework import serializers
from .models import ToolItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolItem
        fields = '__all__'
