from django.db import models
from django.utils.timezone import *
import datetime

class formValue(models.Model):
    formName = models.TextField('Form Name (फारमको नाम)')
    markers = models.IntegerField('Total Markers (प्राप्ताङ्कको जम्मा सङ्ख्या)', default=1)
    formTypeChoices = (
    (1,'House'), (2,'Family'), (3, 'Individual')
    )
    formType = models.IntegerField('Form Target Group',choices=formTypeChoices, default=3)
    jsonText = models.TextField('Json Text')
    def __str__(self):
        return self.formName;

class headings(models.Model):
    formID = models.ForeignKey(formValue, on_delete=models.CASCADE)
    tableName = models.TextField('Table Name (फारमभित्रको टेबलको हेडिङ्ग)')
    weight = models.IntegerField('Order', default=1)
    def __str__(self):
        return self.tableName;

class questions(models.Model):
    simpletext = 'st'
    multiplechoices = 'mc'
    selectchoices = 'sc'
    numberValue = 'nv'
    yesno = 'yn'
    dateformat = 'df'
    answerChoices = ((simpletext, 'Simple Text'),
        (multiplechoices, 'Multiple Choices'),
        (selectchoices, 'Select Choices'),
        (numberValue, 'Number Value'),
        (yesno, 'Yes/No Question'),
        (dateformat, 'मिति Date')
    )
    tableID = models.ForeignKey(headings, on_delete=models.CASCADE)
    question = models.TextField('Question (प्रश्न)')
    answerType = models.CharField(
        max_length=2,
        choices=answerChoices,
        default=yesno,
    )
    # sub_question = models.ForeignKey(questions, on_delete=models.CASCADE, null=True, blank=True)
    marks = models.FloatField('Marks', default=10)
    mandatory=((False,'Yes (खाली छोडे पनि हुने)'), (True, 'No (भर्नै पर्ने)'))
    unanswering = models.BooleanField('उत्तर दिन पर्ने/नपर्ने', default=0,
        choices=mandatory
    )
    description = models.TextField('Description(विवरण)',blank=True, null=True, default='')
    weight = models.IntegerField('Order', default=1)
    choicequestion = models.IntegerField('Parent Choices',blank=True, null=True)
    def __str__(self):
        return self.question;
    def name(self):
        return str(self.id) + "_" + str(self.tableID)

# class subquestion(models.Model):
#     main = models.ForeignKey( questions, on_delete=models.CASCADE, related_name='मुख्य प्रश्न')
#     subquestion = models.ForeignKey(questions, on_delete=models.CASCADE, related_name='दोस्रो प्रश्न')
#     questable = models.ForeignKey(headings, on_delete=models.CASCADE)

class QuestionChoice (models.Model):
    questionID = models.ForeignKey(questions, on_delete=models.CASCADE)
    choiceDescription = models.TextField('Choice')
    weight = models.IntegerField('Order', null=True, blank=True)
    choiceMarks = models.TextField('Choice Marks', null=True, blank=True)
    def __str__(self):
        return self.choiceDescription;
