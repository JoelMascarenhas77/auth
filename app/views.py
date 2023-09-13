from django.shortcuts import render
from . models import info
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def usersignup(request):
    if request.method == "POST":
        username =request.POST['username']
        password = request.POST['password']
        name =request.POST["name"]
        age = int(request.POST["age"])
        
        mystud = info(name=name,age=age)
        mystud.save()
        print(mystud)
        newuser = User.objects.create_user(username =username,key = mystud ,password =password)
        newuser.save()
        return HttpResponseRedirect('')
    return render(request,"signup.html")

def userlogin(request):
    if request.method == "POST":
        username =request.POST['username']
        password = request.POST['password']
        myuser = authenticate(request, username=username, password=password)
        if myuser is not None:
            login(request,myuser)
            return HttpResponseRedirect('/dash/')
    return render(request,"login.html")

@login_required(login_url='/login/')
def dash(request):
    l_user=request.user
    return render(request ,"info.html", {"val1":l_user.id,"val2":l_user.info.name})

def out(requset):
    logout(requset)
    return HttpResponseRedirect('/')

def home(request):
    return render(request, "home.html")
