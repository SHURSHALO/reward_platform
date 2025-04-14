from django.contrib import admin
from api.models import ScheduledReward, RewardLog
from api.tasks import schedule_reward_task


@admin.register(ScheduledReward)
class ScheduledRewardAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'execute_at')
    list_filter = ('execute_at',)
    search_fields = ('user__username',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        schedule_reward_task.apply_async((obj.id,), eta=obj.execute_at)


@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'given_at')
    list_filter = ('given_at',)
    search_fields = ('user__username',)
