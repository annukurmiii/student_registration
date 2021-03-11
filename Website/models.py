from django.db import models

# Create your models here.

class ContactUs(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phoneNo = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email

    
class Student(models.Model):
    studNo = models.AutoField(primary_key=True, default=None)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    emailid = models.EmailField(max_length=150)
    phone = models.IntegerField()
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    batch = models.CharField(max_length=20)
    paymentType = models.CharField(max_length=20)
    fees = models.IntegerField() 

    def __str__(self):
        return self.fname             
