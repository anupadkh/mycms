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
    creator = models.CharField("Creator", max_length=40,default='', blank=True, null = True)
    male_female = (
    (1,'पुरुष । male'), (2,'महिला | Female'), (3, 'तेस्रो लिङ्गि'), (4, 'अन्य'),
    )
    gender = models.IntegerField('लिङ्ग | Gender', choices=male_female, default=1)
    # familyhead = models.IntegerField('Is Family Head', default=0)
    def __str__(self):
        return self.full_name();

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # def __init__(self,request):
    #     self.creator = request.user.username

    def full_name(self):
        if self.mname:
            return self.fname + " " + self.mname + " " + self.lname
        else:
            return self.fname + " " + self.lname
    # class Meta:
    #     app_label = 'Personal Details'
