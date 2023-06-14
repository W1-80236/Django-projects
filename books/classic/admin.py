from django.contrib import admin
from .models import Classicbooks

# Register your models here.
class ClassicsbooksAdmin(admin.ModelAdmin):
    list_display = [ 'bname', 'bqnty', 'bauthor', 'bprice', 'bpublication',  'bpublisheddate']


admin.site.register(Classicbooks,ClassicsbooksAdmin)
