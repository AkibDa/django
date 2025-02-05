from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class OneVarity(models.Model):
  ONE_TYPE_CHOICE = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELACHI'),
  ]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='ones/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=ONE_TYPE_CHOICE)
  description = models.TextField(default='')

  def __str__(self):
    return self.name

# One to Many

class OneReview(models.Model):
  one = models.ForeignKey(OneVarity, on_delete=models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{self.user.username} review for {self.one.name}'
  
# Many to many

class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  one_varities = models.ManyToManyField(OneVarity, related_name='stores')

  def __str__(self):
    return self.name
  
# One to one

class OneCertificate(models.Model):
  one = models.OneToOneField(OneVarity, on_delete=models.CASCADE, related_name='certificate')
  certificate_number = models.CharField(max_length=100)
  issued_date = models.DateTimeField(default=timezone.now)
  valid_until = models.DateTimeField()

  def __str__(self):
    return f'Certificate for {self.name.one}'