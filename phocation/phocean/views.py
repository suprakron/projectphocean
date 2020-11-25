from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def about(request):
   return render(request,'about.html')

@login_required
def zone(request):
    return render(request, 'zone.html')
    	

 
 
def index(request):
   return render(request,'index.html') 

# def login(request):
   # return render(request,'login.html') 


 
def Register(request):
    
	if request.method == 'POST':
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')
		
		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
		# from django.shortcuts import redirect
		return redirect('login')

	return render(request,'signup.html')

@login_required
def karusart(request):
   return render(request,'karusart.html')

@login_required
def logokmitl(request):
   return render(request,'logokmitl.html')

@login_required
def prajom(request):
   return render(request,'prajom.html')

@login_required
def pratep(request):
   return render(request,'pratep.html')

@login_required
def satapat(request):
   return render(request,'satapat.html')

 
def contact(request):
	return render(request, 'contact.html')

@login_required
def engineer(request):
	return render(request, 'engineer.html')

    	
