from django.shortcuts import render
from .models import MovieReview
from django.http import HttpResponse
from django.template import loader

def index(request):
    latest_review_list = MovieReview.objects.order_by('-release_date')[:5]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'moviereview/index.html', context)
def detail(request, review_id):
        review = MovieReview.objects.get(pk=review_id)
        context = {'review': review}
        return render(request, 'moviereview/detail.html',context)