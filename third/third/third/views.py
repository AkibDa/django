from django.http import HttpResponse

def home(request):
  return HttpResponse("Hello, This is home page django")

def about(request):
  return HttpResponse("Hello, This is about page django")

def contact(request):
  return HttpResponse("Hello, This is contact page django")