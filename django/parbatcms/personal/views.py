# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Personal
from .forms import RegistrationForm

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='users:login')
def index(request):
    #1 output = ("Hello, world. You're at the polls index.")
    latest_person_list = Personal.objects.order_by('-pub_date')[:5]
    #2 template = loader.get_template('polls/index.html')
    context = {
        'latest_person_list': latest_person_list,
    }
    return render(request, 'person/index.html', context)
    #2 return HttpResponse(template.render(context, request))

def detail(request,person_id):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        # Do processing
        return HttpResponseRedirect(reverse('personal.views.index'))
    return render(request, 'person/detail.html', {'form': form})
