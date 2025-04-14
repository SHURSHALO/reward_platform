from rest_framework import serializers
from users.models import User
from api.models import RewardLog


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'coins']


class RewardLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = ['amount', 'given_at']
