from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from leaderboard.models import ProblemFilter

from leaderboard.services.honor_farming_service import list_unsolved_problems, ProblemFilterType


# Create your models here.
class SchoolSelectionView(TemplateView):
    template_name = "leaderboard/school_selection.jinja"

class SchoolLeaderboardView(TemplateView):
    template_name = "leaderboard/school_leaderboard.html"

    def get_context_data(self, **kwargs):
        school = self.kwargs.get('school', "I DON'T KNOW")
        tag_name = self.request.GET.get('tag_name', '')
        order_by = self.request.GET.get('order_by', 'tier')
        page_number = int(self.request.GET.get("page", 1))
        allow_unranked = bool(self.request.GET.get('allow_unranked', False))


        query: ProblemFilterType = { 
            'allow_unranked': allow_unranked,
            'school': school,
            'tag_name':  tag_name,
            'order_by': order_by,
        }

        problems = list_unsolved_problems(query)

        paginator = Paginator(problems, 50)
        page_obj = paginator.get_page(page_number)
        filter = ProblemFilter(**{**query, 'page_obj': page_obj})

        context = { 'school': school, 'filter': filter, 'query': filter, 'page_obj': page_obj}

        return context

