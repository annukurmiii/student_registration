from django.contrib import admin
from .models import ContactUs
from .models import Student

# Register your models here.

admin.site.register(ContactUs)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('studNo','fname','lname','emailid','phone','username','password1','password2','gender','address','college','branch','subject','batch','paymentType','fees')
admin.site.register(Student,StudentAdmin)