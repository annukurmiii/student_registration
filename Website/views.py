from django.shortcuts import render, redirect
from .models import ContactUs
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib.auth.models import User
from django.contrib import messages



def home(request):
    return render(request, "home.html", {})

def contactus(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        phoneNo = request.POST['phoneNo']
        email = request.POST['email']
        message = request.POST['message']
        print(name, phoneNo, email, message)

        contactus = ContactUs(name=name, phoneNo=phoneNo, email=email, message=message)
        contactus.save()

    return render(request, "contactus.html")


def register(request): 
    if request.method == 'POST':
        form = StudentForm(request.POST)
    
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            emailid = form.cleaned_data['emailid']
            phone = form.cleaned_data['phone']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            college = form.cleaned_data['college']
            branch = form.cleaned_data['branch']
            subject = form.cleaned_data['subject']
            batch = form.cleaned_data['batch']
            paymentType = form.cleaned_data['paymentType']
            fees = form.cleaned_data['fees']

            s = Student(fname=fname, lname=lname, emailid=emailid, phone=phone, username=username, password1=password1, password2=password2, gender=gender, address=address, college=college, branch=branch, subject=subject, batch=batch, paymentType=paymentType, fees=fees)
            s.save()

            messages.success(request, 'Your account created Successfully')
            messages.info(request, 'Now you can Login')

        else:
            form = StudentForm()

    return render(request, "register.html")

def payment(request):
    return render(request, "payment.html", {})

def aboutus(request):
    return render(request, "aboutus.html", {})

def login(request):
    return render(request, "login.html", {})