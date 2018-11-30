from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from .models import Car
#from adminstrator.models import register
from adminstrator.models import mydata
# Create your views here.

def home(request):
	context = {}
	return render(request, 'home/home.html', context)

def charts(request):
	context={}
	return render(request, 'home/highchart.html', context)



def about(request):
	context = {}
	return render(request, 'home/about.html', context)


def gallery(request):
	context = {}
	return render(request, 'home/gallery.html', context)

def booking(request):
	carList = Car.objects.all().order_by("-id")
	context = {'carLst':carList}
	return render(request, 'adminstrator/booked.html', context)


def contact(request):

	context = {}

	if request.method == 'POST':

		subject = request.POST["subject"]
		message = request.POST["message"]
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [request.POST["email"]]
		#send_mail( subject, message, email_from, recipient_list)
		context = {'message':"We will contact you shortly."}


	return render(request, 'home/contact.html', context)


def login(request):
	context={}

	if request.method == 'POST':
		username=request.POST["username"]
		password=request.POST["password"]
		user = User.objects.get(username__exact=self.username)

		valid =check_password(cleaned_data['password'])
		if not valid:
			raise forms.ValidationError("Password Incorrect")
		return valid
	return render(request, 'home/login.html', context)	

	   	


def service(request):
	context = {}
	return render(request, 'home/service.html', context)


def elements(request):
	context = {}
	return render(request, 'home/elements.html', context)


def cars(request):
	carList = Car.objects.all().order_by("-id")[:3]
	context = {'carLst':carList}
	return render(request, 'home/cars.html', context)


def addcar(request, carid = 0):

	if request.method == 'POST' and request.FILES['carimage']:
		carname = request.POST["name"]
		msi = request.POST["msi"]
		price = request.POST["price"]
		capacity  = request.POST["capacity"]
		aircondition  = request.POST["aircondition"]
		transmission  = request.POST["transmission"]
		description  = request.POST["description"]
		carimage = request.FILES['carimage']
		fs = FileSystemStorage()
		filename = fs.save(carimage.name, carimage)
		carimagename = fs.url(filename)

		carObject = Car()
		carObject.name = carname
		carObject.msi = msi
		carObject.description = description
		carObject.price = price
		carObject.capacity = capacity
		carObject.aircondition = aircondition
		carObject.transmission = transmission
		carObject.carimage = carimagename

		carObject.save()



	context = {}

	if carid > 0:
		editCarObject  = Car.objects.get(id=carid)
		context = {'editCarObject':editCarObject}

	
	return render(request, 'home/addcar.html', context)


def blog1(request):
	context = {}
	return render(request, 'home/blog1.html', context)


def blog2(request):
	context = {}
	return render(request, 'home/blog2.html', context)

def deletecar(request, carid):

	Car.objects.filter(id=carid).delete()
	return redirect('/carlist')

def updatecar(request):

	if request.method == 'POST':
		carid = request.POST["hdnCarId"]
		carname = request.POST["name"]
		msi = request.POST["msi"]
		price = request.POST["price"]
		capacity  = request.POST["capacity"]
		aircondition  = request.POST["aircondition"]
		transmission  = request.POST["transmission"]
		description  = request.POST["description"]

		if len(request.FILES) > 0 :
			carimage = request.FILES['carimage']
			fs = FileSystemStorage()
			filename = fs.save(carimage.name, carimage)
			carimagename = fs.url(filename)
		else :
			carimagename = request.POST["hdnImage"]


		updateCarObject = Car.objects.get(id=carid)
		updateCarObject.name = carname
		updateCarObject.msi = msi
		updateCarObject.description = description
		updateCarObject.price = price
		updateCarObject.capacity = capacity
		updateCarObject.aircondition = aircondition
		updateCarObject.transmission = transmission
		updateCarObject.carimage = carimagename

		updateCarObject.save()

	return redirect('/carlist')









