from django.db import models
from django.utils.timezone import *
import datetime

'''
Personal
Address
Nagrikta
Contact
Media # Online Media
Hobby

'''
class Personal(models.Model):
    fname = models.CharField('पहिलो नाम',max_length=100)
    mname = models.CharField('विचको नाम',max_length=50, blank=True, null=True)
    lname = models.CharField('अन्तिमको नाम',max_length=100)

    pub_date = models.DateTimeField('Date Published')
    gened = models.CharField('Generated Id', max_length=60, default="23", blank=True, null=True) #Generated IDS
    creator = models.IntegerField(default=0)
    # familyhead = models.IntegerField('Is Family Head', default=0)
    def __str__(self):
        return self.full_name();

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # class Meta:
        # appname = "Person"

    def full_name(self):
        if self.mname:
            return self.fname + " " + self.mname + " " + self.lname
        else:
            return self.fname + " " + self.lname
    # class Meta:
    #     app_label = 'Personal Details'



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
    number = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    reg_date = models.CharField(max_length=10)
    card_type = models.IntegerField('Type of Card', default=1)
    def __str__(self):
        return self.number

class Contact(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    contact_type = models.IntegerField('Type of Contact', default=1)

class Social(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    social_type = models.IntegerField('Media Type', default=1)

class Hobby(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    skills = models.CharField(max_length=50)
    timespent = models.CharField(max_length=100)
