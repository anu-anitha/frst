from django.shortcuts import render,redirect
from . models import Stu 
from . forms import StuForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='login')
def home(request):
	data=Stu.objects.all()  
	context={"data":data} 
	return render(request,"home.html",context)


def update(request,id):
	z = Stu.objects.get(pk=id)
	form = StuForm(instance=z) #old data
	if request.method == 'POST':
		form = StuForm(request.POST, instance=z)
		if form.is_valid():
			form.save()
			return redirect('/app/home/')
	context = {'form':form}
	return render(request, 'update.html', context)

def delete(request, id):
	Stu.objects.get(pk=id).delete()
	messages.info(request,"data deleted")
	return render(request, 'delete.html')
	

def read(request,id):
	print(id)
	dynamicdata = Stu.objects.get(pk=id)
	context = {'data':dynamicdata}   
	return render(request, 'read.html', context)



def create(request):#POST
	form = StuForm()
	if request.method == 'POST':#TRUE
		# breakpoint()
		print(request.POST)
		form = StuForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			print('data saved')
		return redirect("/app/home/")
	context = {'form':form}
	return render(request, 'create.html', context)


def signup(request):
	form = SignupForm()
	if request.method == 'POST':#TRUE
		print(request.POST)
		form = SignupForm(request.POST)
		if form.is_valid():
			# breakpoint()
			form.save()
	context = {'form':form}
	return render(request, 'signup.html', context)


def loginn(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username = username,password = password)
		if user is not None:
			login(request,user)
			if request.user.is_authenticated:
				username = request.user.username
				messages.info(request, "Welcome "+username)
			return redirect('/home/home')
	return render(request, 'login.html')


def logoutt(request):#get
	logout(request)
	return redirect('/')