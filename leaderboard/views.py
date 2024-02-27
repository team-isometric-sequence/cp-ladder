from django.views.generic.base import TemplateView


# Create your models here.
class SchoolSelectionView(TemplateView):
    template_name = "leaderboard/school_selection.html"

class SchoolLeaderboardView(TemplateView):
    template_name = "leaderboard/school_leaderboard.html"

    def get_context_data(self, **kwargs):
        school = self.kwargs.get('school', "I DON'T KNOW")
        context = { 'school': school }
        print(context)
        return context

