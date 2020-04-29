from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.forms import UserCreationForm

app_name = 'userapp'
def login_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/user/')
    else:
        form = UserCreationForm()
        return render(request,'userapp/login.html',{'form':form})


def register(request):
    return render(request,'userapp/register.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("userapp:homepage")

class UserView(View):
    form_class = UserForm
    template_name = 'userapp/user.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/')

        return render(request, self.template_name, {'form' : form})

def home(request):
    msg="GOOD LUCK"
    return render(request,"userapp/home.html",{'msg':msg})
