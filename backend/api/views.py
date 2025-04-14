from datetime import timedelta
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import ScheduledReward, RewardLog
from api.serializers import ProfileSerializer, RewardLogSerializer
from api.tasks import schedule_reward_task



class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


class RewardListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RewardLogSerializer

    def get(self, request):
        rewards = RewardLog.objects.filter(user=request.user)
        serializer = self.serializer_class(rewards, many=True)
        return Response(serializer.data)


class RewardRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        now = timezone.now()

        if RewardLog.objects.filter(
            user=user, given_at__date=now.date()
        ).exists():
            return Response(
                {'detail': 'Можно запрашивать награду только 1 раз в день'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        execute_at = now + timedelta(minutes=5)
        scheduled = ScheduledReward.objects.create(
            user=user, amount=10, execute_at=execute_at
        )

        schedule_reward_task.apply_async((scheduled.id,), eta=execute_at)

        return Response({'detail': 'Награда будет начислена через 5 минут'})
