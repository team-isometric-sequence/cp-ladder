from django.urls.conf import path

from leaderboard.views import SchoolLeaderboardView, SchoolSelectionView


urlpatterns = [ 
    path('', SchoolSelectionView.as_view()),
    path('leaderboard/<str:school>', SchoolLeaderboardView.as_view(), name="school-leaderboard")
]
