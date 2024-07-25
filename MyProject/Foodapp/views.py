from django.shortcuts import render
from django.http import HttpResponse
from Foodapp.models import Details

# Create your views here.
def welcome(request):
    return HttpResponse('Hello from Django app...!!')
def message(requsest):
    return Httpresponse("<h1>Message from django...!!</h1>")
def home(request):
    items=Details.objects.all()
    context={
        'items' :items,
    }
    return render(request,'home.html',context)
def register(request):
    return render(request,'register.html')
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        register=Details(username=username,email=email,phone=phone)
        register.save()
    return render(request,'register.html')