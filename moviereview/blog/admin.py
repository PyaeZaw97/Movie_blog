from django.contrib import admin
from .models import MovieReview
class MovieReviewAdmin(admin.ModelAdmin):
	list_display = ('movie_title', 'movie_poster','genre','release_date','running_time','nomination_prize','movie_rating','nationality','rate','review','director','actor','actress','user_view','reviewer')
admin.site.register(MovieReview,MovieReviewAdmin)
# Register your models here.
