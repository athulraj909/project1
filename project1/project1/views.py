from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import *

def index(request):
    return render(request,'index.html')

def first(request):
    return render(request,'index.html')

def userreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=userdetails(name=name,phone=phone,email=email,image=image,password=password)
        registration.save()
    return render(request,'register.html',{'succes':'registered suucessfully'})

def contactreg(request):
    tem=request.session['uid']
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        contactreg=contactdetails(name=name,phone=phone,email=email,image=image,userid=tem)
        contactreg.save()
    return render(request,'contact.html',{'succes':'saved successfully'})

def uview(request):
    users=userdetails.objects.all()
    return render(request,'user view.html',{'res':users})

def contacview(request):
    temp=request.session['uid']
    user=contactdetails.objects.filter(userid=temp)
    return render(request,'contactview.html',{'res':user})


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return render(request, 'index.html')

    elif userdetails.objects.filter(email=email,password=password).exists():
        userdetail=userdetails.objects.get(email=request.POST['email'], password=password)
        if userdetail.password == request.POST['password']:
            request.session['uid'] = userdetail.id
            request.session['uname'] = userdetail.name

            request.session['email'] = email

            request.session['user'] = 'user'

            return render(request,'index.html')
        
    else:
        return render(request, 'loginform.html', {'status': 'Invalid Username or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
      del request.session[key]
    return redirect(index)


def delete(request,id):
    member = userdetails.objects.get(id=id)
    member1 = contactdetails.objects.filter(userid=member.id)
    member.delete()
    member1.delete()
    return redirect(uview)

def remove(request,id):
    member = contactdetails.objects.get(id=id)
    member.delete()
    return redirect(contacview)


def contactedit(request):
    return render(request,'contact edit.html')

def userpro(request):
    tem=request.session['uid']
    vpro=userdetails.objects.get(id=tem)
    return render(request,'userprofile.html',{'result':vpro})

def useredi(request):
    return render(request,'useredit.html')

def adminprofil(request):
    return render(request,'adminprofile.html')

def updat(request,id):
    upt=userdetails.objects.get(id=id)
    return render(request,'useredit.html',{'result':upt})

def updates(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        password=request.POST.get('password')
        registration=userdetails(name=name,phone=phone,email=email,image=image,password=password,id=id)
        registration.save()
        return redirect(userpro)
    
def updt(request,id):
    upt=contactdetails.objects.get(id=id)
    return render(request,'contact edit.html',{'res':upt})


def contactupdate(request,id):
    tem=request.session['uid']
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        contactreg=contactdetails(name=name,phone=phone,email=email,image=image,userid=tem,id=id)
        contactreg.save()
        return redirect(contacview)