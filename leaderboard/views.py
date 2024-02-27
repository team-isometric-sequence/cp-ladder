from django.views.generic.base import TemplateView

# Create your models here.
class SchoolSelectionView(TemplateView):
    template_name = "leaderboard/school_selection.html"
