from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from  django.contrib.auth import authenticate,logout
from  django.contrib.auth import login
from .models import AddItem,ItemList
from django.contrib import messages
from .filters import AddItemfilter
from .forms import CreateUserForm,Additemform
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request,"index.html")

def register(request):
	if request.method =='POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()		
			return redirect('login')			
						
	else:
		form = CreateUserForm
	return render(request, "register.html", {'form':form})


@login_required(login_url='login')
def base(request):				
		Addeditem = request.user.itemlist.all()		
		my_filter = AddItemfilter(request.GET, queryset=Addeditem)
		Addeditem = my_filter.qs
		context ={'Addeditem':Addeditem,'AddItemfilter':my_filter}	
		return render(request, 'base.html',context)
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
@login_required(login_url='login')
def add(request):	
	form = Additemform()
	if request.method=="POST":
		form = Additemform(request.POST)		
		if form.is_valid():
			name = form.cleaned_data['item_name']	
			quantity = form.cleaned_data['item_quantity']
			status = form.cleaned_data['item_gaze']
			status2= form.cleaned_data['item_dimensions']
			date  = form.cleaned_data['Date']			
			t = ItemList(item_name=name,item_quantity=quantity,item_gaze=status,item_dimensions=status2,Date=date)
			t.save()
			request.user.itemlist.add(t)
			user = request.user
			template = render_to_string('thanks.html',{'name':name,'quantity':quantity,'status':status,'status2':status2,'Date':date,'user':user})
			email = EmailMessage(
				'Hey! You got an order',
				template,
				settings.EMAIL_HOST_USER,
				['powerbabu2015@gmail.com',
				'sureshnvn143@gmail.com'],

			)	
			email.fail_silently = False
			email.send()									
			print("item added")
			messages.success(request, ("Item has been added to the basket!"))
			return redirect('base')
		else:
			return render(request, 'add.html',{'form':form})
	return render(request,'add.html',{'form':form})

def update(request,pk):
	Addeditem = ItemList.objects.get(id=pk)
	form = Additemform(instance=Addeditem)
	context = {"form":form}
	if request.method=='POST':
		form = Additemform(request.POST,instance=Addeditem)
		if form.is_valid():
			form.save()
			return redirect("base")
	return render(request, 'update.html',context)

def delete(request,pk):
	item = ItemList.objects.get(id=pk)
	context = {'item':item}
	if request.method=='POST':
		item.delete()
		return redirect('base')

	return render(request,"delete.html",context)

