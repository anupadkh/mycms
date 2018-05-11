from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required

from .forms import *
from django.http import Http404



# Create your views here.
@login_required(login_url='users:login')
def index(request):
    #2 template = loader.get_template('polls/index.html')
    context = {

    }
    return render(request, 'design/index.html', context)
    #2 return HttpResponse(template.render(context, request))

def entry(request, person=0):
    if person!=0:
        my_person = Personal.objects.get(pk = int(person))
        form = PersonalForm(request.POST or None, instance=my_person)
    else:
        form = PersonalForm(request.POST or None)
    if form.is_valid():
        person_saved = form.save()
        return redirect('formentry:people_status', status=1)
    return render (request, 'design/forms.html',{'form':form, 'user':request.user, 'personid':person})

def all_people(request, status=0):
    a = Personal.objects.all()
    if status==1:
        status_name = "Saved"
    else:
        status_name = None
    return render (request, 'design/all.html', {'user':request.user,  'status':status_name, 'all':a})
