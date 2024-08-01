from rest_framework import serializers
from .models import Events, Registration

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        # fields = ('id', 'name', 'description', 'date', 'location')
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        # fields = ('id', 'user', 'event', 'attendance', 'registered_at')