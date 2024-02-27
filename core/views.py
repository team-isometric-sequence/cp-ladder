from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class SampleView(TemplateView):
    template_name = "example/sample.html"
