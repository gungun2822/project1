
from django.shortcuts import render, redirect
from application.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):

    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('message')

        info = enquiry_table(name = a, email = b, phone = c, message = d)

        info.save()

        messages.success(request, 'Enquiry form has been sent successfully')

    return render(request, 'contact.html')


def login_user(request):

    if request.method =='POST':
        a = request.POST.get('username')
        b = request.POST.get('password')

        user = authenticate(request, username = a, password = b)

        if user is not None:
            login(request, user)
            
            return redirect('dashboard')

        else:
            messages.error(request, 'In-correct username or password!..')
    return render(request, 'login.html')


def dashboard(request):

    
    return render(request, 'dashboard/index.html')

def enquiry_details(request):

    info = enquiry_table.objects.all()

    dict = {'information':info}

    return render(request, 'dashboard/tables.html', dict)
def delete_record(request,id):
    if request.method=='POST':
        data=enquiry_table.objects.get(pk=id)
        data.delete()

    return HttpResponseRedirect('/enquiry-details/')
def edit_record(request,id):
    info=enquiry_table.objects.filter(pk=id)
    dt={ 'information':info}
    return render(request,'dashboard/edit_record.html',dt)

def update_record(request,id):
    info=enquiry_table.objects.get(pk=id)
    info.name=request.POST.get('name')
    info.email=request.POST.get('email')
    info.phone=request.POST.get('phone')
    info.message=request.POST.get('message')
    info.save()
    return HttpResponseRedirect('/enquiry-details/')