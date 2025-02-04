from django.shortcuts import render

# Create your views here.
def all_one(request):
  return render(request, 'one/all_one.html')