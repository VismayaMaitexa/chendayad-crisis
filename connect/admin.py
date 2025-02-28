from django.contrib import admin
from . models import userdetails,donationrequest,Admindonation,donationvolunteer
# Register your models here.
admin.site.register(userdetails)
from . models import volunteerdetails,OTP
admin.site.register(volunteerdetails)
from . models import Crisisreporting
admin.site.register(Crisisreporting)
from . models import jobdetails
admin.site.register(jobdetails)
admin.site.register(donationrequest)
admin.site.register(Admindonation)
admin.site.register(donationvolunteer)
admin.site.register(OTP)
