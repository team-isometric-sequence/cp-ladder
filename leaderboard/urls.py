from django.urls.conf import path

from leaderboard.views import SchoolSelectionView


urlpatterns = [ 
    path('', SchoolSelectionView.as_view())
]
