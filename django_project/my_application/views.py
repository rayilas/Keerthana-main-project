from django.shortcuts import render
from django.http import HttpResponse
from .models import Datas
# Create your views here.



def register(request):
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
        obj.Conform_Password=password
        obj.save()
    return render(request,"signup.html")



