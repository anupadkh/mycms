from django.shortcuts import render, get_object_or_404

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

def entry(request):
    form = PersonalForm(request.POST or None)
    if form.is_valid():
        return HttpResponseRedirect(reverse('formentry.views.index'))
    return render (request, 'design/forms.html',{'form':form})
