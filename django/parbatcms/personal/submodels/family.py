from django.db import models
from personal.models import Personal

'''
Family
GeoCode
Relation

'''
class GeoCode(models.Model):
    latitude = models.CharField('Latitude',max_length=30)
    longitude = models.CharField('Longitude',max_length=30)
    def __str__(self):
        return full_coordinates()

    def full_coordinates(self):
        return self.latitude + ", " + self.longitude;

class House(models.Model):
    coordinates = models.ForeignKey(GeoCode, on_delete = models.CASCADE)
    owner = models.ForeignKey(Personal, on_delete = models.CASCADE)

class Family(models.Model):
    person = models.ForeignKey(Personal, on_delete = models.CASCADE)
    #head of the family
    gened = models.CharField(max_length=50, blank=True, null=True)
    myhouse = models.ForeignKey(House, on_delete = models.CASCADE)
    def __str__(self):
        return self.person.full_name();


class Relation(models.Model):
    person1 = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='familyhead')
    person2 = models.ForeignKey(Personal, on_delete=models.CASCADE)
    relntype = models.CharField(max_length=50)
    def __str__(self):
        return self.relntype
