from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  #return HttpResponse("Hello, This is home page django")
  return render(request, 'websites/index.html')

def about(request):
  return HttpResponse("Hello, This is about page django")

def contact(request):
  return HttpResponse("Hello, This is contact page django")