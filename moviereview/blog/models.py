from django.db import models

class MovieReview(models.Model):
	movie_title=models.CharField(max_length=200)
	movie_poster=models.ImageField()
	genre=models.CharField(max_length=100)
	release_date=models.CharField(max_length=100)
	running_time=models.CharField(max_length=50)
	nomination_prize=models.CharField(max_length=200)
	movie_rating=models.CharField(max_length=200)
	nationality=models.CharField(max_length=200)
	rate=models.CharField(max_length=200)
	review=models.TextField()
	director=models.CharField(max_length=200)
	actor=models.CharField(max_length=200)
	actress=models.CharField(max_length=200)
	user_view=models.CharField(max_length=200)
	reviewer=models.CharField(max_length=200)
