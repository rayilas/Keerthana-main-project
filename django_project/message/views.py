from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def message(request):
    return render(request,'message.html')

def success(request):
    messages.success(request,'This is Success Message')
    return render(request,'message.html')
