from django.db import models
from personal.models import Personal

'''
Family
GeoCode
Relation

'''
class Family(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    #head of the family
    gened = models.CharField(max_length=50)
    def __str__(self):
        return self.person.full_name();

class GeoCode(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)

class Relation(models.Model):
    # person1 = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='familyhead')
    person2 = models.ForeignKey(Personal, on_delete=models.CASCADE)
    relntype = models.IntegerField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    geolocation = models.ForeignKey(GeoCode, on_delete=models.CASCADE,blank=True, null=True)
