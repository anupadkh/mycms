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
    fname = models.CharField('First Name',max_length=100)
    lname = models.CharField('Last Name',max_length=100)
    mname = models.CharField('Middle Name',max_length=50, blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    gened = models.CharField('Generated Id', max_length=60, default="23", blank=True, null=True) #Generated IDS
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
        # app_label = 'Personal Details'



class Address(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    addr_type = models.IntegerField(default=1) #permanent or temporary
    country = models.CharField(max_length=20)
    district = models.CharField(max_length=40)
    house = models.IntegerField(default=0)
    palika = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    def __str__(self):
        return self.palika

class Nagrikta(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    number = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    reg_date = models.CharField(max_length=10)
    def __str__(self):
        return self.number

class Contact(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

class Media(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    online = models.IntegerField()
    username = models.CharField(max_length=30)

class Hobby(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    skills = models.CharField(max_length=50)
    timespent = models.CharField(max_length=100)
