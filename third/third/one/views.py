from django.shortcuts import render, get_object_or_404
from .models import OneVarity, Store
from .forms import OneVarityForm

# Create your views here.
def all_one(request):
  ones = OneVarity.objects.all()
  return render(request, 'one/all_one.html', {'ones': ones})

def one_detail(request, one_id):
  one = get_object_or_404(OneVarity, pk=one_id)
  return render(request, 'one/one_details.html', {'one':one})

def one_store_view(request):
  stores = None
  if request.method == 'POST':
    form = OneVarityForm(request.POST)
    if form.is_valid():
      one_variety = form.cleaned_data['one_varity']
      stores = Store.objects.filter(one_varieties=one_variety)
  else:
    form = OneVarityForm()
  return render(request, 'one/one_stores.html', {'stores': stores, 'form': form})