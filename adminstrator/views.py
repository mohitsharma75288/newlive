from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings


from .decorator import my_user_required
from home.models import Car

from .models import mydata
from home.models import books
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

#@my_user_required
#@login_required(login_url='/adminstrator/deco')
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

	
	return render(request, 'adminstrator/addcar.html', context)




#@login_required(login_url='/login/')
def charts(request):
	context={}
	return render(request, 'adminstrator/highchart.html', context)

def signup(request):

	if request.method == 'POST':
		firstname= request.POST["firstname"]
		lastname = request.POST["lastname"]
		country = request.POST.get("country")
		usertype = request.POST.get("usertype")
		email = request.POST["email"]
		username  = request.POST["username"]
		password  = request.POST["password"]
		
		ds1Obj =mydata()
		ds1Obj.fname = firstname
		ds1Obj.lname = lastname
		ds1Obj.country= country
		ds1Obj.utype= usertype
		ds1Obj.email= email
		ds1Obj.username = username
		ds1Obj.password = password
		
		ds1Obj.save()

	context={}
	return render(request, 'adminstrator/register.html', context)

def booked(request):
	if request.method=='POST':
		name=request.POST["name"]
		email=request.POST["email"]
		phone=request.POST["phone"]
		from_destination=request.POST["destination"]
		to_destination=request.POST["destinations"]
		datetime=request.POST["datetime"]
		dsobj=books()
		dsobj.name=name
		dsobj.email=email
		dsobj.phone=phone
		dsobj.adestination=from_destination
		dsobj.bdestination=to_destination
		dsobj.datetime=datetime
		dsobj.save
	context={}
	return render(request, 'adminstrator/booked.html', context)


def dashboard(request):
	context={}
	return render(request, 'adminstrator/dashboard.html', context)


def booking(request):
	carList = Car.objects.all().order_by("-id")
	context = {'carLst':carList}
	return render(request, 'adminstrator/booked.html', context)




def user(request):
	context={}
	return render(request, 'adminstrator/user.html', context)

def upgrade(request):
	context={}
	return render(request, 'adminstrator/upgrade.html', context)

def carlist(request):
	carList = Car.objects.all().order_by("-id")
	context = {'carLst':carList}
	return render(request, 'adminstrator/carlist.html', context)


def table(request):
	context={}
	return render(request, 'adminstrator/table.html', context)


def typography(request):
	context={}
	return render(request, 'adminstrator/typography.html', context)

def maps(request):
	context={}
	return render(request, 'adminstrator/maps.html', context)

def notifications(request):
	context={}
	return render(request, 'adminstrator/notifications.html', context)


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











