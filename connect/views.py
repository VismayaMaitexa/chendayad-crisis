from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import*
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html') 
            

def admins(request):
    return render(request,'admins.html')

from.forms import UserForm 
def user_view(request):
    if request.method== 'POST':
        form=UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form=UserForm()
    return render(request,'user.html',{'form':form})
 
from.forms import VolunteerForm
def volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('volunteerlist')
        else:
            # Print form errors to console
            print(form.errors)
    else:
        form = VolunteerForm()

    return render(request, 'volunteer.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . models import userdetails,JobApplication
from django.contrib.auth.models import User  # Assuming you are using Django's default User model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .models import userdetails,volunteerdetails  # Import your userdetails model

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = userdetails.objects.get(username=username)

            if user.password == password:  # In a real-world scenario, use password hashing!
                request.session['user_id'] = user.id  # Store user ID in the session
                messages.success(request, f"Welcome, {username}!")
                return redirect('userdashboard')  
            else:
                messages.error(request, "Incorrect password.")
        except userdetails.DoesNotExist:
            messages.error(request, "Username does not exist.")

    return render(request, 'userlogin.html') 

def userdashboard(request):
    print(request.user,'jhgjhhjlk')
    return render(request, 'userdashboard.html')

def volunteerlogin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = volunteerdetails.objects.get(username=username)

            if user.password == password:  # In a real-world scenario, use password hashing!
                request.session['user_id'] = user.id  # Store user ID in the session
                messages.success(request, F"Welcome, {username}!")
                return redirect('volunteerdashboard')  
            else:
                messages.error(request, "Incorrect password.")
        except volunteerdetails.DoesNotExist:
            messages.error(request, "Username does not exist.")

    return render(request, 'volunteerlogin.html') 


def volunteerdashboard_view(request):
    objects=Admindonation.objects.all()
    return render(request, 'volunteerdashboard.html',{"objects":objects})

def crisis (request):
    approved_reports = Crisisreporting.objects.filter(status='approved')
    
    return render(request, 'crisis.html', {
        'approved_reports': approved_reports.order_by('-id'),
    })


def volunteerhelp (request):
    return render(request,'volunteerhelp.html')

from django.shortcuts import render, redirect
from .forms import CrisisreportingForm


# views.py

# views.py

from django.shortcuts import render, redirect
from .forms import CrisisreportingForm
from .models import Crisisreporting
from .forms import JobForm
def crisisreporting(request):
    if request.method == 'POST':
        form = CrisisreportingForm(request.POST, request.FILES)
        if form.is_valid():
            # Assign the logged-in user to the user field before saving
            crisis_report = form.save(commit=False)  # Don't save immediately
            crisis_report.user = request.user  # Set the current user
            crisis_report.save()  # Now save the instance
            return redirect('crisissuccess')
        else:
            print(form.errors,'errrrr')  # For debugging, print errors if form is invalid
    else:
        form = CrisisreportingForm()

    return render(request, 'crisisreporting.html', {'form': form})


def resourcerequest (request):
    if request.method=='POST':
        user_id=request.session.get('user_id')
        user=get_object_or_404(userdetails,id=user_id)


        name=request.POST.get('name')
        category=request.POST.get('category')
        quantity=request.POST.get('quantity')
        donationrequest.objects.create(name=name,category=category,quantity=quantity,user=user)
        return redirect('success_page')

    return render(request,'resourcerequest.html')

def users (request):
    return render(request,'users.html')
def volunteers (request):
    return render(request,'volunteers.html')
def crisisreports (request):
    return render(request,'crisisreports.html')
def logout (request):
    return render(request,'index.html')
def admindashboard(request):
    return render(request, 'admindashboard.html')

# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Hardcoded username and password
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect('admindashboard')
        else:
            return HttpResponse("Invalid credentials, please try again.", status=401)
    return render(request, 'admins.html')
# views.py

from django.shortcuts import render, redirect
from .forms import CrisisreportingForm
from .models import Crisisreporting

def add(request):
    if request.method == 'POST':
        form = CrisisreportingForm(request.POST, request.FILES)
        if form.is_valid():
            # Assign the logged-in user to the user field before saving
            crisis_report = form.save(commit=False)
            crisis_report.user = request.user
            crisis_report.status = 'approved'  # Set the status to pending initially
            crisis_report.save()
            return redirect('view')
    else:
        form = CrisisreportingForm()
    return render(request, 'add.html', {'form': form})
# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Crisisreporting,jobdetails

def approve(request):
    # Fetch all pending reports
    pending_reports = Crisisreporting.objects.filter(status='pending')
    approved_reports = Crisisreporting.objects.filter(status='approved')  # Fetch approved reports

    if request.method == 'POST':
        action = request.POST.get('action')
        report_id = request.POST.get('report_id')
        report = Crisisreporting.objects.get(id=report_id)
        district=report.location

        if action == 'approve':
            report.status = 'approved'
            subject = "Crisis alert"
            content = {'content': 'content','report':report}
            template = "./crisis_mail.html"
            mail_list = volunteerdetails.objects.filter(district=district).values_list('email', flat=True)
            print(mail_list)

            email_recipients = list(mail_list)  
            status=send_email(
            template=template,
            subject=subject,
            recipients=email_recipients,
            content=content,
            bulk=True,
            
            )
            report.save()
        elif action == 'reject':
            report.delete()

        return redirect('view')

    return render(request, 'approve.html', {
        'pending_reports': pending_reports,
        'approved_reports': approved_reports,
    })

def view(request):
    approved_reports = Crisisreporting.objects.filter(status='approved').order_by('-id')
    
    return render(request, 'view.html', {
        'approved_reports': approved_reports,
    })


def volunteercrisis (request):
    approved_reports = Crisisreporting.objects.filter(status='approved')
    vol=get_object_or_404(volunteerdetails,id=request.session.get('user_id'))
    
    return render(request, 'volunteercrisis.html', {
        'approved_reports': approved_reports.filter(location=vol.district).order_by('-id'),
    })


def volunteercrisisreporting(request):
    if request.method == 'POST':
        form = CrisisreportingForm(request.POST, request.FILES)
        if form.is_valid():
            # Assign the logged-in user to the user field before saving
            crisis_report = form.save(commit=False)  # Don't save immediately
            crisis_report.user = request.user  # Set the current user
            crisis_report.save()  # Now save the instance
            return redirect('crisisreporting')
        else:
            print(form.errors)  # For debugging, print errors if form is invalid
    else:
        form = CrisisreportingForm()

    return render(request, 'volunteercrisisreporting.html', {'form': form})



def crisisvolunteer(request):
 return render(request,'crisisvolunteer.html')

def job(request):
   approved_reports =jobdetails.objects.filter(status='pending')
    
   return render(request, 'job.html', {
        'approved_reports': approved_reports,
    })
  

def adminjob(request):
  if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            # Assign the logged-in user to the user field before saving
            job_report = form.save(commit=False)  # Don't save immediately
            job_report.user = request.user  # Set the current user
            job_report.save()  # Now save the instance
            return redirect('adminjob')
        else:
            print(form.errors)  # For debugging, print errors if form is invalid
  else: 
        form =JobForm()

  return render(request, 'adminjob.html', {'form': form})

def adminreport(request):
  return render(request,'adminreport.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def userprofile(request):
    user = get_object_or_404(userdetails, id=request.session.get('user_id'))

    if request.method == 'POST':
        # Get the data from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        district = request.POST.get('district')

        # Update the user's profile with the new data
        user.username = username
        if password and password != '':
            user.password = password  
        user.phone = phone
        user.city = city
        user.pincode = pincode
        user.district = district
        user.save()

        # Redirect to the profile page after saving
        return redirect('userprofile')

    context = {
        'user': user
    }
    return render(request, 'userprofile.html', context)


def volunteerprofile(request):
    user = get_object_or_404(volunteerdetails, id=request.session.get('user_id'))

    if request.method == 'POST':
        # Get the data from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        district = request.POST.get('district')
        email = request.POST.get('email')
        bloodgroup = request.POST.get('bloodgroup')

        # Update the user's profile with the new data
        user.username = username
        if password and password != '':
            user.password = password  
        user.phone = phone
        user.city = city
        user.email=email
        user.bloodgroup=bloodgroup
        user.pincode = pincode
        user.district = district
        user.save()

        # Redirect to the profile page after saving
        return redirect('volunteerprofile')

    context = {
        'user': user
    }
    return render(request, 'volunteerprofile.html', context)




def useredit(request):
  return render(request,'useredit.html')

def volunteeredit(request):
  return render(request,'volunteeredit.html')


def volunteerdonation(request,post_id):
    post=get_object_or_404(Admindonation,id=post_id)
    if request.method=='POST':
        volunteer_id=request.session.get('user_id')
        quantity=request.POST.get('donationAmount')
        volunteer=get_object_or_404(volunteerdetails,id=volunteer_id)
        donationvolunteer.objects.create(user=volunteer,quantity=quantity,donation=post)
        return redirect('volunteerdashboard')
    print('hii')
    return render(request, 'volunteerdonation.html',{'post':post})


def userdonation(request):
    # Handle POST request (if form is submitted)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new volunteer details to the database
            return redirect('userdonation')  # Redirect to the same page after saving
    else:
        form = UserForm()

    # Retrieve all volunteer details to display
    users = userdetails.objects.all()

    return render(request, 'userdonation.html', {
        'form': form,  # Pass the form to the template
        'users': users,  # Pass the list of volunteers to the template
    })




def jobs_view(request):
    return render(request,'jobs.html')

def job(request):
    user_id = request.session.get('user_id')
    print(user_id)

    approved_reports = jobdetails.objects.all()
    
    for item in approved_reports:
        application = JobApplication.objects.filter(user__id=user_id, job=item)
        if application.exists():
            item.application_status = application.first().status

    # Send the updated queryset to the front end
    return render(request, 'job.html', {
        'approved_reports': approved_reports,
    })


def job_approve_volunteer(request,job_id):
    user_id=request.session.get('user_id')
    user=get_object_or_404(volunteerdetails,id=user_id)
    job=get_object_or_404(jobdetails,id=job_id)

    if JobApplication.objects.filter(user=user,job=job,status='approved').exists():
        return redirect('job')
    
    try:
        JobApplication.objects.create(user=user,job=job,status='approved')
    except Exception as e:
        print(e)
        return redirect ('job')
    return redirect('job')



def job_reject_volunteer(request,job_id):
    user_id=request.session.get('user_id')
    user=get_object_or_404(volunteerdetails,id=user_id)
    job=get_object_or_404(jobdetails,id=job_id)

    application=JobApplication.objects.filter(user=user,job=job)

    if application.exists():
        obj=application.first()
        obj.status='rejected'
        obj.save()
        return redirect('job')
    
    try:
        JobApplication.objects.create(user=user,job=job,status='rejected')
    except Exception as e:
        print(e)
        return redirect ('job')
    return redirect('job')

from django.shortcuts import render
from .models import jobdetails

def joblist(request):
    # Get the top 5 jobs
    jobs = jobdetails.objects.all()[:5]  # Limit the results to the first 5
    print(jobs)
    return render(request, 'job_list.html', {'jobs': jobs})

def admin_list_job_applications(request,job_id):
    applications=JobApplication.objects.filter(status='approved',job__id=job_id)
    return render(request,'job_applications.html',{'applications':applications})


def adminjob(request):
  if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            # Assign the logged-in user to the user field before saving
            job_report = form.save(commit=False)  # Don't save immediately
            job_report.user = request.user  # Set the current user
            job_report.save()  # Now save the instance
            return redirect('job_list')
        else:
            print(form.errors)  # For debugging, print errors if form is invalid
  else: 
        form =JobForm()

  return render(request, 'adminjob.html', {'form': form})

def adminreport(request):
  return render(request,'adminreport.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse

# View to accept the job
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import jobdetails

@login_required
def accept_job(request, job_id):
    try:
        job = jobdetails.objects.get(id=job_id)
    except jobdetails.DoesNotExist:
        return HttpResponse("Job not found", status=404)

    if job.status != 'pending':
        return HttpResponse("This job is no longer available", status=400)

    job.status = 'approved'
    job.save()  # Save the updated job status
    return redirect('job_list')  # Redirect to the job list view where all jobs are shown


def reject_job(request, job_id):
    try:
        job = jobdetails.objects.get(id=job_id)
    except jobdetails.DoesNotExist:
        return HttpResponse("Job not found", status=404)
    
    job.status = 'rejected'
    job.save()
    return redirect('job')  


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # If using Django's built-in User model
from django.contrib import messages

def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()  # Deletes the user from the database
        messages.success(request, 'User deleted successfully!')
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
    
    return redirect('users')  # Redirect back to the users page or wherever you want


# views.py

from django.shortcuts import render, redirect
from .models import volunteerdetails
from django.http import Http404

def delete_volunteer(request, id):
    try:
        volunteer = volunteerdetails.objects.get(id=id)
    except volunteerdetails.DoesNotExist:
        raise Http404("Volunteer does not exist")
    
    # Check if the request method is POST to confirm deletion
    if request.method == 'POST':
        volunteer.delete()
        return redirect('volunteers')  # Redirect to the volunteer list page
    
    return render(request, 'confirm_delete.html', {'volunteer': volunteer})

def userlist(request):
    users=userdetails.objects.all()
    return render(request,'userlist.html',{'users':users})


def volunteerlist(request):
    users=volunteerdetails.objects.all()
    return render(request,'volunteerlist.html',{'users':users})


def admindonation(request):
    donations=donationrequest.objects.all()
    return render(request,'donationrequest.html',{'requests':donations})


def accept_donations(request,donation_id):
    donation=get_object_or_404(donationrequest,id=donation_id)
    donation.adminapprove=True
    donation.save()
    return redirect('donationrequest')

def reject_donations(request,donation_id):
    donation=get_object_or_404(donationrequest,id=donation_id)
    donation.delete()
    return redirect('donationrequest')

def admindonate(request):
     queryset=Admindonation.objects.all()
     return render(request,'admindonate.html',{'posts':queryset})


def admindonateadd(request):
     if request.method=='POST':

        item_name=request.POST.get('item_name')
        category=request.POST.get('category')
        quantity=request.POST.get('quantity')
        Admindonation.objects.create(item_name=item_name,category=category,quantity=quantity)
        return redirect('admindonate')

     return render(request,'add_donationpost.html')


def donationrequestvolunteer(request):
      set=donationvolunteer.objects.all()
      return render(request,'donationrequestvolunteer.html',{'posts':set})


def accept_donationvolunteer(request,donation_id):
    donation=get_object_or_404(donationvolunteer,id=donation_id)
    donation.adminapprove=True
    donation.save()
    return redirect('donationrequestvolunteer')

def reject_donationvolunteer(request,donation_id):
    donation=get_object_or_404(donationvolunteer,id=donation_id)
    donation.delete()
    return redirect('donationrequestvolunteer')


import random
import string

def generate_otp(length=6):
    otp = ''.join(random.choices(string.digits, k=length))
    return otp


from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_email(template, subject, content, recipients, bulk=False):
    sender = settings.EMAIL_HOST_USER
    try:
        html_content = render_to_string(template, content)
        text_content = strip_tags(html_content)

        if bulk:
            msg = EmailMultiAlternatives(subject, text_content, from_email=sender, to=recipients)
            msg.attach_alternative(html_content, 'text/html')
            msg.bcc = recipients 
        else:
            msg = EmailMultiAlternatives(subject, text_content, from_email=sender, to=[recipients])
            msg.attach_alternative(html_content, 'text/html')

        msg.send()
        print('Mail sent successfully')
        return True
    except Exception as e:
        print(e, 'Mail not sent')
        return False

def password_reset(request):
    # Check if the request method is POST
    if request.method == 'POST':
        mail = request.POST.get('email')
        otp=generate_otp()
        
        recipient = mail
        subject = "Otp from crisis connect"
        content = {'content': 'content','otp':otp}
        template = "./mail.html"
        
        status=send_email(
            template=template,
            subject=subject,
            recipients=recipient,
            content=content,
            
        )
        if status == True:
            obj,_=OTP.objects.get_or_create(email=mail)
            obj.otp=otp
            obj.save()
            return redirect('verify_otp',otp_id=obj.id)
        
    return render(request, 'password_reset.html')


def verify_otp(request,otp_id):
    error_message=''
    if request.method=="POST":
        otp_obj=get_object_or_404(OTP,id=otp_id)
        enterd_otp=int(request.POST.get('otp')) if request.POST.get('otp') else 0

        if otp_obj.otp == enterd_otp:
            return redirect('set_new_password',pk=otp_obj.id)
        else:
            error_message = "Invalid OTP. Please try again."


    return render(request,'otp_verify.html',{'otp_id':otp_id,'error':error_message})


def set_new_password(request,pk):
    if request.method == 'POST':
        otp_obj=get_object_or_404(OTP,id=pk)
        password=request.POST.get('password')
        volunteer=get_object_or_404(volunteerdetails,email=otp_obj.email)
        volunteer.password=password
        volunteer.save()
        return redirect('volunteerlogin')
    return render(request,'new_password.html',{'pk':pk})




def volunteerregister(request):
    return render(request,'volunteerregister.html')



def chatbot(request):
    return render(request,'chatbot.html')

def location(request,re_id):
    report=get_object_or_404(Crisisreporting,id=re_id)
    return render(request,'location.html',{'lat':report.lat,'long':report.long})

from .models import userdetails

from . import models  

def delete_user(request, user_id):
    user = models.userdetails.objects.get(id=user_id)  
    user.delete() 
    return redirect('user_list')  

def crisisreportinguser (request):
    return render(request,'crisisreportinguser.html')


def delete_volunteers(request, volunteer_id):
    user = models.volunteerdetails.objects.get(id=volunteer_id)  
    user.delete() 
    return redirect('volunteerlist')



def registervolunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('volunteerlogin')
        else:
            # Print form errors to console
            print(form.errors)
    else:
        form = VolunteerForm()

    return render(request, 'registervolunteer.html', {'form': form})



from django.shortcuts import render
from .models import donationrequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import donationrequest, userdetails
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def success_page(request):
    return render(request, 'success.html')

def crisissuccess(request):
    return render(request, 'crisissuccess.html')
