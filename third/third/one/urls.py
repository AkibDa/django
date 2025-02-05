from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_one, name='all_one'),
    path('<int:one_id>/', views.one_detail, name='one_detail'),
]