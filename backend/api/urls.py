from django.urls import path
from api.views import ProfileView, RewardListView, RewardRequestView


urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('rewards/', RewardListView.as_view()),
    path('rewards/request/', RewardRequestView.as_view()),
]
