from django.db import models
from django.contrib.auth.models import User

class Places(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    general_price = models.FloatField(null=True)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class InterestsActivities(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isGuide = models.BooleanField(default=False)
    place_of_stay = models.ForeignKey(Places, on_delete=models.CASCADE, related_name="guide_play_of_stay", null=True)
    searching_for = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    interestCount = models.IntegerField(default=0)
    places_of_interest = models.ManyToManyField(Places, related_name='user_places_of_interest')
    interests = models.ManyToManyField(InterestsActivities, related_name='InterestsActivities')

class Hiring(models.Model):
    traveller = models.ForeignKey(CustomUser, related_name='hiring_traveller', on_delete=models.SET_NULL, null=True)
    guide = models.ForeignKey(CustomUser, related_name='hiring_guide', on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(Places, related_name='hiring_place', on_delete=models.SET_NULL, null=True)
    pay = models.FloatField(null=True)
