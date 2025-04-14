from celery import shared_task
from api.models import ScheduledReward, RewardLog


@shared_task
def schedule_reward_task(scheduled_id):
    try:
        reward = ScheduledReward.objects.get(id=scheduled_id)
        user = reward.user
        user.coins += reward.amount
        user.save()
        RewardLog.objects.create(user=user, amount=reward.amount)
        reward.delete()
    except ScheduledReward.DoesNotExist:
        pass
