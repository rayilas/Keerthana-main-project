from django.shortcuts import render
from django.http import HttpResponse
from .models import Datas
from .models import Login
# Create your views here.



def signup(request):
    if request.method=='POST':

        Firstname=request.POST['Firstname']
        Lastname=request.POST['Lastname']
        Email=request.POST['Email']
        Password=request.POST['Password']
        password=request.POST['password']


        obj=Datas()
        obj.First_Name=Firstname
        obj.Last_Name=Lastname
        obj.Email=Email
        obj.Password=Password
        obj.Confirm_Password=password
        obj.save()
    return render(request,"signup.html")

def login(request):
    if request.method=='POST':

        Email=request.POST['Email']
        Password=request.POST['Password']

        obj1=Login()
        obj1.Emailid=Email
        obj1.EmailPassword=Password
        obj1.save()
    return render(request,"login.html")







