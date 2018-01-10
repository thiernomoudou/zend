from rest_framework import serializers

from .models import DeliveryBookingModel

class DeliveryBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryBookingSerializer