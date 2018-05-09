from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout


# Create your views here.
def index(request):
    context = {}
    return render(request,'users/index.html',context)


def login_view(request):
    #Loggin in the UsersConfig
    if request.method=='POST':
        #Do sth
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('formentry:index')

    else:
        #instantiate
        form = AuthenticationForm()

    return render(request,'users/index2.html',{'form':form})

def signup_view(request):
    # #Signup new user
    if request.method=='POST':
        #Do sth
        # logger.error('This was valid bro')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user = form.get_user
            login(request, user)
            return redirect('personal:index')

    else:
        #instantiate
        form = UserCreationForm()
        # form = 'This page is under Construction'

    return render(request,'users/index2.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('users:login')
