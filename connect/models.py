from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class userdetails(models.Model):
    username=models.CharField(max_length=20,null=False,default="username")
    password=models.CharField(max_length=20,null=False,default="password")
    phone=models.CharField(max_length=20,null=False)      
    city = models.CharField(max_length=50, null=False,default="city")
    pincode = models.CharField(max_length=10, null=False,default="abv")
    district = models.CharField(max_length=50, null=False,default="district")
    
    # For file upload
    aadhar_file = models.FileField(upload_to='aadhar_files/', null=True, blank=True)


class volunteerdetails(models.Model):
    username = models.CharField(max_length=20, null=False, default="username")
    password = models.CharField(max_length=20, null=False, default="password")
    phone = models.CharField(max_length=10, null=False)
    email = models.EmailField()
    bloodgroup = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=50, null=False,default="city")
    pincode = models.CharField(max_length=6, null=False,default="abv")
    district = models.CharField(max_length=50, null=False,default="district")
    
    # For file upload
    aadhar_file = models.FileField(upload_to='aadhar_files/', null=True, blank=True)

    def __str__(self):
        return self.username



from django.db import models

# models.py

from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
class Crisisreporting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # This field cannot be NULL
    message = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    lat=models.FloatField(default=0)
    long=models.FloatField(default=0)
    disasterimage = models.ImageField(upload_to='disaster_images/', null=True, blank=True)
    affectedpeoples = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message

class admindetails(models.Model):
    username=models.CharField(max_length=20,null=False,default="username")
    password=models.CharField(max_length=20,null=False,default="password")


from django.utils import timezone
class jobdetails(models.Model):
    location=models.CharField(max_length=50,null=False,default="location")
    message=models.CharField(max_length=40,null=False,default="message")
    vacancy=models.CharField(max_length=40,null=False,default="vacancy")
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ])
    created_at = models.DateTimeField(default=timezone.now)


class JobApplication(models.Model):
    job=models.ForeignKey(jobdetails,on_delete=models.CASCADE,related_name='application_job')
    user=models.ForeignKey(volunteerdetails,on_delete=models.CASCADE,related_name='application_user',null=True,blank=True)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ])

    def __str__(self):
        return f"Application for{self.job.message} by{self.user.username}"
    

class donationrequest(models.Model):
    user = models.ForeignKey(userdetails, on_delete=models.CASCADE,null=True,blank=True) 
    name=models.CharField(max_length=150,null=True,blank=True)
    category = models.CharField(max_length=50)
    quantity = models.CharField(max_length=20)
    adminapprove=models.BooleanField(null=True,blank=True)

    created_at = models.DateTimeField(default=timezone.now)

class Admindonation(models.Model):
    item_name=models.CharField(max_length=150,null=True,blank=True)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    recieved_quantity=models.IntegerField(default=0)

class donationvolunteer(models.Model):
    user = models.ForeignKey(volunteerdetails, on_delete=models.CASCADE,null=True,blank=True) 
    quantity = models.CharField(max_length=20)
    donation=models.ForeignKey(Admindonation,on_delete=models.CASCADE,null=True,blank=True)
    adminapprove=models.BooleanField(null=True,blank=True)


class OTP(models.Model):
    otp = models.IntegerField(null=True,blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.email
