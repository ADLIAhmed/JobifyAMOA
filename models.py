from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class offre(models.Model):
    offre_title=models.CharField(max_length=200)
    offre_contenu=models.TextField()
    offre_ville=models.CharField(max_length=50)
    offre_renumeration = models.CharField(max_length=200)
    offre_periode = models.CharField(max_length=200)

from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
	Name=models.CharField(max_length=264)
	Age=models.PositiveIntegerField()
	PhoneNumber=models.CharField(unique=True,max_length=128)
	Email=models.EmailField(unique=True)
	Addresse=models.CharField(max_length=264)
class Description(models.Model):
	desc_text=models.CharField(max_length=500)
	#def __str__(self):
		#return self.top_name

class Portfolio(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	Portfolio_name=models.CharField(max_length=264)
	image=models.ImageField()
	Type=models.CharField(max_length=264)
	date=models.DateField()

class Skill(models.Model):
	Name=models.ForeignKey(User,on_delete=models.CASCADE)
	skill_name=models.CharField(max_length=264)
	Level=models.CharField(max_length=264)

class Experience(models.Model):
	Name=models.ForeignKey(User,on_delete=models.CASCADE)
	exp_name=models.CharField(max_length=264)
	Type=models.CharField(max_length=264)
	date=models.DateField()

class Education(models.Model):
	Name=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateField()
	School=models.CharField(max_length=264)





class Rating(models.Model):
	Name=models.ForeignKey(User,on_delete=models.CASCADE)
	Text_comment=models.CharField(max_length=300)
	date=models.DateField()

from django.db import models
from django.contrib.auth.models import User




class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    subcategory1 = models.TextField()
    subcategory2 = models.TextField()
    subcategory3 = models.TextField()


def __str__(self):
    return self.name
    


class Available_services(models.Model):
    s_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def getdescription(self):
        return self.description
    

class Registred_employers(models.Model):
    performer_id  = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    
    
    def getPhoneNumber(self):
        return self.phone
    
    def getEmail(self):
        return self.email

    def getFirstName(self):
        return self.first_name
    
    def getLastname(self):
        return self.last_name
        
class Registred_employees(models.Model):
    employee_id  = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    employment = models. CharField(max_length=30)
    hourly_price = models.FloatField()
    
    
    def getPhoneNumber(self):
        return self.phone
    
    def getEmail(self):
        return self.email

    def getFirstName(self):
        return self.first_name
    
    def getLastname(self):
        return self.last_name
    
    def getEmployment(self):
        return self.employment
    
    def getPrice(self):
        return self.hourly_price


class Finished_Services(models.Model):
    finished_service_id = models.IntegerField(primary_key=True)
    service_id = models.ForeignKey(to=Available_services, on_delete=models.CASCADE)
    who_did_it = models.ForeignKey(to=Registred_employers, on_delete=models.CASCADE)
    for_who = models.ForeignKey(to=Registred_employees, on_delete=models.CASCADE)
    started_date = models.DateTimeField()
    finished_date = models.DateTimeField()
    
    def started_date_serv(self):
        return self.started_date
    
    def finished_date_serv(self):
        return self.finished_date
    
    
    

