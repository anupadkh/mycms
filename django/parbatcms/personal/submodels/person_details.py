from django.db import models
from personal.models import Personal

class Address(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    addr_type = models.IntegerField('Temporary or Permanent',default=1) #permanent or temporary
    country = models.CharField('Country',max_length=20,default="Nepal")
    district = models.CharField('District',max_length=40)
    house = models.IntegerField('House No', blank=True, null=True)
    palika = models.CharField('Municipality',max_length=20)
    state = models.CharField('State',max_length=30)
    def __str__(self):
        return self.palika

class Nagrikta(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    number = models.CharField("कार्ड नं", max_length=160)
    district = models.CharField("जारी गर्ने जिल्ला", max_length=160)
    reg_date = models.CharField("जारी मिति", max_length=160, blank=True, null=True)
    exp_date = models.CharField("म्याद सकिने मिति", max_length=160, blank=True, null=True)
    card_type = models.IntegerField('कार्डको प्रकार', default=1)
    def __str__(self):
        return self.number

class Contact(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    email = models.CharField("इमेल", max_length=100)
    phone = models.CharField("फोन नं", max_length=100)
    contact_type = models.IntegerField('Type of Contact', default=1)

class Social(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    social_type = models.IntegerField('Media Type', default=1)

class Hobby(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    skills = models.CharField(max_length=50)
    timespent = models.CharField(max_length=100)
