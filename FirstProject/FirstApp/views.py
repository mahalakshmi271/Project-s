
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register

# Create your views here.
def home(request):
	return HttpResponse("HI GOOD EVENING TO ALL....")

def bootstrapfun(request):
	return render(request,'html/sampleboot.html')

def regform(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		number=request.POST['number']
		gender=request.POST['gender']
		address=request.POST['address']
		lang=request.POST.getlist('check')
		data={'firstname':fname,'lastname':lname,'emailId':email,'phonenumber':number,'gender':gender,'address':address,'languages':lang}
		return render(request,'html/display.html',data)
	return render(request,'html/regform.html')


def btregi(request):
	return render(request,'html/btregst.html')


def register1(request):
	#name='asha'
	#email'asha123@gmail.com'
	reg=Register(name="teja",email="teja123@gmail.com")
	reg.save()
	return HttpResponse("row inserted sucessfully...")

def register2(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		reg=Register(name=name,email=email)
		reg.save()
	return HttpResponse("Record inserted sucessfully")
	return render(request,'html/register2.html')

def display(request):
	data=Register.objects.all()
	return render(request,'html/display1.html',{'data':data})

def sview(request,y):
	w=Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	#return HttpResponse("Your id is: {} and Your email is: {}".format(w.name,w.email))


def supt(request,q):
	t=Register.objects.get(id=q)
	if request.method=='POST':
		na=request.POST['n']
		em=request.POST['e']
		t.name=na
		t.email=em
		t.save()
		return redirect('/display')
		#print(na,em,t.name,t.email)
	return render(request,'html/supdate.html',{'p':t})


def sudl(request,p):
	b=Register.objects.get(id=p)
	if request.method=="POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndlt.html',{'z':b})


