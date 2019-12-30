from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import MovieReview
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'review/index.html'
    context_object_name = 'review_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return MovieReview.objects.order_by('-release_date')[:5]
# Create your views here.
