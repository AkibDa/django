from django.shortcuts import render, get_object_or_404
from .models import OneVarity

# Create your views here.
def all_one(request):
  ones = OneVarity.objects.all()
  return render(request, 'one/all_one.html', {'ones': ones})

def one_detail(request, one_id):
  one = get_object_or_404(OneVarity, pk=one_id)
  return render(request, 'one/one_details.html', {'one':one})