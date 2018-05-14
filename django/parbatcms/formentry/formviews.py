from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.contrib.auth.decorators import login_required

from .designforms import *
from django.http import Http404
from formentry.submodals.formGenerator import *

@login_required(login_url='users:login')
def mainforms(request,form_id,formtype,member):
    return render(request, 'base_forms/base.html')

login_required(login_url='users:login')
def index(request):
    myforms = formValue.objects.all()
    newLink = '/forms/design/'+'0/main/'
    return render(request,'base_forms/list.html',{'new': newLink, 'list':myforms, 'form_type':'form'})

login_required(login_url='users:login')
def formindex(request,id):
    if id!=0:
        forminstance = formValue.objects.get(id=id)
        savedform = forminstance
        #next url addition
        nextPage = '/forms/design/' + str(id) + '/table/'
    else:
        forminstance = None
        nextPage = None
    form = mainForm(request.POST or None, instance=forminstance)
    if form.is_valid():
        savedform = form.save()
        id= savedform.id
    url = '/forms/design/' + str(id) +'/main/'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'next': nextPage})

login_required(login_url='users:login')
def tableindex(request,id):
    try:
        tables = headings.objects.filter(formID=id)
    except headings.DoesNotExist:
        redirect(request,'formentry:submit_tableindex',tid=0, formid=id)
    newLink = '/forms/design/'+str(id)+'/form/0/mytable'
    return render(request,'base_forms/list.html',{'new': newLink, 'list':tables, 'formid':id, 'tab_type':'table'})

login_required(login_url='users:login')
def submit_tableindex(request,tid,formid):
    id=tid
    mainform = formValue.objects.get(id=formid)
    if id==0:
        try:
            table = headings.objects.get(id=tid)
        except headings.DoesNotExist:
            table = headings(formID=mainform)
    else:
        table = headings.objects.get(id=tid)
    form = tableForm(request.POST or None, instance=table)
    if form.is_valid():
        saved_table = form.save()
        return redirect('formentry:submit_tableindex', formid=mainform.id, tid=saved_table.id)
    url = '/forms/design/' + str(formid) +'/form/'+ str(id) + '/mytable/'
    nextPage = '/forms/design/' + str(id) + '/question'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'next': nextPage, 'tab_type': 'table'})

login_required(login_url='users:login')
def questionindex(request,id):
    try:
        tables = questions.objects.filter(tableID=id)
    except questions.DoesNotExist:
        redirect(request,'formentry:submit_questionindex',qid=0, tid=id)
    newLink = '/forms/design/'+str(id)+'/table/0/myquestion'
    return render(request,'base_forms/list.html',{'new': newLink, 'list':tables, 'tid':id, 'ques_type': 'question' })

login_required(login_url='users:login')
def submit_questionindex(request,tid,qid):
    #copied from submit_tableindex mainform: maintable, table:question, saved_table: saved_question
    id=qid
    mainform = headings.objects.get(id=tid)
    if id==0:
        try:
            table = questions.objects.get(id=qid)
        except questions.DoesNotExist:
            table = questions(tableID=mainform)
    else:
        table = questions.objects.get(id=qid)
    form = questionForm(request.POST or None, instance=table)
    if form.is_valid():
        saved_table = form.save()
        return redirect('formentry:submit_questionindex', tid=mainform.id, qid=saved_table.id)
    url = '/forms/design/' + str(tid) +'/table/'+ str(id) + '/myquestion/'
    nextPage = '/forms/design/' + str(id) + '/choice'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'next': nextPage})

login_required(login_url='users:login')
def choiceindex(request,id):
    try:
        choices = QuestionChoice.objects.filter(questionID=id)
    except QuestionChoice.DoesNotExist:
        redirect(request,'formentry:submit_choiceindex',cid=0, qid=id)
    newLink = '/forms/design/'+str(id)+'/question/0/mychoice'
    return render(request,'base_forms/list.html',{'new': newLink, 'list':choices, 'qid':id, 'choice_type': 'choice' })

login_required(login_url='users:login')
def submit_choiceindex(request,cid,qid):
    newLink = '/forms/design/'+str(qid)+'/question/0/mychoice/'
    id=cid
    mainform = questions.objects.get(id=qid)
    if id==0:
        try:
            choice = QuestionChoice.objects.get(id=id)
        except QuestionChoice.DoesNotExist:
            choice = QuestionChoice(questionID=mainform)
    else:
        choice = QuestionChoice.objects.get(id=id)
    form = choiceForm(request.POST or None, instance=choice)
    if form.is_valid():
        saved_choice = form.save()
        return redirect('formentry:submit_choiceindex', qid=mainform.id, cid=saved_choice.id)
    url = '/forms/design/' + str(qid) +'/question/'+ str(id) + '/mychoice/'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'new':newLink})

@login_required(login_url='users:login')
def designform(request,form_id=0):
    if form_id==0:
        return render(request, 'base_forms/base.html')
