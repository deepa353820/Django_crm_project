from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import signupform
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    # form = UserCreationForm()
    form = signupform()
    return render(request,'Authenticationapp/signup.html',{'form':form})


def home_signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Or wherever you want to redirect
    else:
        form = signupform()

    return render(request, 'Authenticationapp/signup.html', {'form': form})

@login_required
def home(request):
    return render(request,'Authenticationapp/home.html')





# def login(request):
#     return render(request,'base.html')
