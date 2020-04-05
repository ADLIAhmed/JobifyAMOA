from django.shortcuts import render
from Jobify_app.models import User,Portfolio,Description
from . import forms
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'Homepage/Home.html')
def postanoffer(request):
    return render(request, 'Postanoffer/index.html')
def test(request):
    return render(request, 'Test/test.html')
def categories(request):
    return render(request, 'Categories/categories.html')
def payment(request):
    return render(request, 'GSJ/payment.html')
def responsepayment(request):
    return render(request, 'GSJ/payment_response.html')
def offre(request):
    return render(request, 'Offre/index.html')
def registration(request):
    return render(request, 'Registration/index.html')
def profil(request):
    return render(request, 'Profil/index.html')
def login(request):
    return render(request, 'Login/index.html')
def confirmation(request):
    return render(request, 'Confirmation/confirmation.html')
def confirmationhire(request):
    return render(request, 'Confirmationhire/confirmationhire.html')
def confirmationpayment(request):
    return render(request, 'Confirmationpayment/Confirmationpayment.html')
def offreetudiant(request):
    return render(request, 'Offre2/offreetudiant.html')
def confirmationinteresse(request):
    return render(request, 'Confirmationinteresse/confirmationinteresse.html')
def interesse(request):
    return render(request, 'Interesse/interesse.html')
def profils(request):
    return render(request, 'Profils/profils.html')
def offrepersonnalisee(request):
        return render(request, 'OffreP/offre.html')


from django.shortcuts import render, redirect
from datetime import date
from GSJ.models import Registred_employers,Finished_Services,Registred_employees,Available_services

# Create your views here.


############################################################################################################
##  from django.http import HttpResponse                                                                  ##
##  def home():                                                                                           ##
##      return HttpResponse("Hello! I'd like to welcome everyone to our NEW service Global Students Job") ##
############################################################################################################



def payment(request):
    user_id = 1
    user = Registred_employers.objects.get(performer_id=user_id)
    who = user.first_name + " " + user.last_name
    email = user.email
    company = user.company
    f_services = Finished_Services.objects.filter(who_did_it=user_id)
    services = []
    service = dict()
    Total = 0
    for ser in f_services:
        serv = Available_services.objects.get(s_id=ser.service_id.s_id)
        empl = Registred_employees.objects.get(employee_id=ser.for_who.employee_id)
        
        service['Name'] = serv.name
        service['Employee'] = empl.first_name + " " + empl.last_name
        service['PricePerHour'] = "{:.2f}".format(empl.hourly_price)
        service['Employment'] = empl.employment
        service['SDate'] = ser.started_date
        service['FDate'] = ser.finished_date
        Total += empl.hourly_price
        services += [service]
        service = dict()
    return render(request,"GSJ/payment.html",{'Email':email,'UserFullName':who,'Company':company,'Services':services,'Total':Total})

def payment_response(request):
    return render(request,"GSJ/payment_response.html")


    
        

"""
path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), """

"""
def index(request):
	return render(request,'Jobify_app/index.html')

def form_name_view(request):
	form=forms.FormName()
	desc=forms.FormDescription()
	port=forms.FormPortfolio()
	if request.method=='POST':
		form=forms.FormName(request.POST)
		port=forms.FormPortfolio(request.POST)
		desc=forms.FormDescription(request.POST)
	return render(request,'Jobify_app/profile_edit.html',{'form':form,'desc':desc,'port':port})
def profile_edit(request):
	user_list=User.objects.order_by('Name')
	user_dict={'users':user_list}
	return render(request,'Jobify_app/profile_edit.html',context=user_dict)
def form_desc_view(request):
	desc=forms.FormDescription()
	if request.method=='POST':
		desc=forms.FormDescription(request.POST)
	return render(request,'Jobify_app/profile_edit.html',{'desc':desc})
def form_portfolio_view(request):
	port=forms.FormPortfolio()
	if request.method=='POST':
		port=forms.FormDescription(request.POST)
	return render(request,'Jobify_app/profile_edit.html',{'port':port})



# form_desc_view(request):
	#form=forms.UpdateFormDesc()
	#if request.method=='POST':
		#form=forms.UpdateFormDesc(request.POST)
		#if form.is_valid():
			#print("validation success!")
			#print("Description:",form.cleaned_data['desc_text'])
	#return(render(request,'basicapp/form_page.html',context={'form':form}))     """
	
