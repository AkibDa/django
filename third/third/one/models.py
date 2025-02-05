from django.db import models
from django.utils import timezone

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
