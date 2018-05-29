from django.shortcuts import render


# def uploadfile(request, ):

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from .forms import *
from .models import *

from pprint import pprint

@login_required(login_url='users:login')
def simple_upload(request, member, memberType):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # model_instance = form.save(commit=False)
            form.save()
            # model_instance.im
            # pprint(model_instance.document)
            return redirect('formentry:index')
    else:
        myinstance = ImageUploads(member=member, memberType=memberType)
        # myinstance.upload()
        pprint(myinstance)
        form = DocumentForm(instance=myinstance)
    # return render(request, 'core/model_form_upload.html', {
    #     'form': form
    # })
    return render(request, 'photo/index.html', {
        'form':form
    })
