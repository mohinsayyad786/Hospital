from django.shortcuts import render,redirect
from django.http import HttpResponse
from sperohelthapp.models import Task
from sperohelthapp.form import RegisterForm
from django.views import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from sperohelthapp.models import Task

# Create your views here.


def homes(request):

    return render(request,"home.html")



def index(request):

    content={}
    #content['data']=Task.objects.all()
    #print(content['data'])
    content['data']=Task.objects.filter(is_deleted='N')

    return render(request,'index.html',content)



def addpt(request):

    if request.method=='POST':
        p=request.POST['p']
        t=request.POST['t']
        ps=request.POST['ps']
        em=request.POST['em']
        l=request.POST['l']

        t1=Task.objects.create(hhc_id=p,patients_name=t,mobile_no=ps,email=em,location=l,is_deleted='N')
        #print(t1)
        t1.save()
        return redirect('/')
    else:



        return render(request,'addpt.html')

def delete(request,rid):

    x=Task.objects.filter(id=rid)
    x.update(is_deleted='Y')
    return redirect('/')



def edit(request,rid):

    if request.method=='POST':
        up=request.POST['p']
        ut=request.POST['t']
        ups=request.POST['ps']
        uem=request.POST['em']
        ul=request.POST['l']
        #print(up)
        #print(ut)
        #print(ups)
        #print(uem)
        #print(ul)
        x=Task.objects.filter(id=rid)
        x.update(hhc_id=up,patients_name=ut,mobile_no=ups,email=uem,location=ul)
        return redirect('/')


    else:
        content={}
        content['data']=Task.objects.filter(id=rid)
        return render(request,'editpt.html',content)

    



def register(request):

    if request.method=='POST':
       
       fm=RegisterForm(request.POST)
       #print(fm)
       #print(fm.is_valid())
       if fm.is_valid():
            messages.success(request,'Account created Successfully,Please login!!!')
            fm.save()
            return redirect('/register')
            return HttpResponse('Pls Signup First')

    else:
        fm=RegisterForm()
        return render(request,'signup.html',{'form':fm})



def user_login(request):
    if request.method=="POST":
        current_user = request.user
        user_id = current_user.id
        print(user_id)
        context = {'user_id': user_id}
        fm=AuthenticationForm(request=request,data=request.POST)
        #print(fm)
        #print(fm.is_valid())
        if fm.is_valid():
            
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            #print(uname)
            #print(upass)
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u:
                login(request,u)

                return redirect('/')

        return HttpResponse('Pls Signup First')
        
    else:
        fm=AuthenticationForm()


        return render(request,'login.html',{'form':fm})

def user_logout(request):
    logout(request)

    return redirect('/login')

def search(request):
    query = request.GET['query']
    #allposts = Task.objects.all()
    data = Task.objects.filter(patients_name__icontains=query)
    params = {'data': data}
    return render(request,'search.html',params)

def searchmobile(request):
    query = request.GET['mobile']
    #allposts = Task.objects.all()
    data = Task.objects.filter(mobile_no__icontains=query)
    params = {'data': data}
    return render(request,'search.html',params)



    