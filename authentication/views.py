from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import TokenGenerator, generate_token
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is not Matching")
            return render(request,'authentication/signup.html')
        try:
            if User.objects.get(username=email): 
                messages.info(request,"User already exists")
                return render(request,'authentication/signup.html')
        except Exception as identifier:
            pass
        user= User.objects.create_user(name,email,password,)
       
        user.save()
        
        return redirect('/auth/login/')
    return render(request,"authentication/signup.html")




def handlelogin(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is None:
             messages.error(request,"Invalid Credential")
             return redirect('/auth/login')
           
        
        else:
             login(request,myuser)
             messages.success(request,"Loged in Successfully")
             return redirect('/')
           
        
    return render(request,"authentication/login.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout successfully")
    return redirect('/auth/login')
