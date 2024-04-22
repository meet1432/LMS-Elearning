from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app.EmailBackEnd import EmailBackEnd

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        #check email
        if User.objects.filter(email=email).exists():
           messages.warning(request,'Email are Already Exists !')
           return redirect('register')
        
        # check username
        if User.objects.filter(username=username).exists():
           messages.warning(request,'Username are Already exists !')
           return redirect('register')
        
        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        messages.success(request,'Account Created Successfully !')
        return redirect('login')

    return render(request, 'registration/register.html')

	
def DoLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = EmailBackEnd.authenticate(request,username=email,password=password)
        if user == None:
           login(request,user)
           messages.success(request,'Login Successfully !')
           return redirect('home')
        else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')
	
    return render(request, 'registration/login.html')
	   
		   
  