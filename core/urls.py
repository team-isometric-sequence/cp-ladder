from django.urls import path
from core.views import SampleView

urlpatterns = [
    path("sample", SampleView.as_view()),
]
