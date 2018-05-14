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
    form = mainForm(None)
    url = '/forms/design/0/main/'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url})

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
    url = '/forms/design/' + str(savedform.id) +'/main/'
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'next': nextPage})

login_required(login_url='users:login')
def tableindex(request,id):
    try:
        tables = headings.objects.filter(formID=id)
    except headings.DoesNotExist:
        redirect(request,'formentry:submit_tableindex',tid=0)
    newLink = '/forms/design/'+str(id)+'/form/0/mytable'
    return render('base_forms/list.html',{'new': newLink, 'list':tables})

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
    return render(request, 'base_forms/design.html',{'form':form, 'url':url, 'next': nextPage})


@login_required(login_url='users:login')
def designform(request,form_id=0):
    if form_id==0:
        return render(request, 'base_forms/base.html')
