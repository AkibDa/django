from django.contrib import admin
from .models import OneVarity, OneReview, OneCertificate, Store

# Register your models here.
class OneReviewInLine(admin.TabularInline):
  model = OneReview
  extra = 2

class OneVarietyAdmin(admin.ModelAdmin):
  list_display = ('name','type','date_added')
  inlines = [OneReviewInLine]

class StoreAdmin(admin.ModelAdmin):
  list_display = ('name', 'location')
  filter_horizontal = ('one_varities',)

class OneCertificateAdmin(admin.ModelAdmin):
  list_display = ('chai','certificate_number')


admin.site.register(OneVarity, OneVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(OneCertificate, OneCertificateAdmin)
admin.site.register(OneReview, OneReviewInLine)
