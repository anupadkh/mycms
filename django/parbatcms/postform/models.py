from django.db import models
from formentry.submodals.formGenerator import *

# Create your models here.
class formEntries(models.Model):
    formfield = models.ForeignKey(questions, on_delete=models.CASCADE)
    answers = models.CharField('उत्तर', max_length=150)
    member = models.IntegerField('आइ डी')
    form = models.ForeignKey(formValue, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.formfield) + ": " +  str(self.answers)

class MarkValues(models.Model):
    valueid = models.ForeignKey(formEntries, on_delete=models.CASCADE)
    marker = models.CharField('प्रश्नकर्ता', max_length=40)
    marks = models.FloatField('Marks')
    def __str__(self):
        return str(self.valueid) + ": " + str(self.marks)
