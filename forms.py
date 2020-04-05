from django import forms
from .models import offre

class offre_form(forms.ModelForm):
    class offre:
        model = offre
        fields = [
            'offre_title',
            'offre_contenu',
            'offre_ville',
            'offre_renumeration',
            'offre_periode',
        ]


from django.contrib.auth.models import User

class FormName(forms.Form):
	Name=forms.CharField()
	Age=forms.IntegerField()
	Email=forms.CharField()
	PhoneNumber=forms.CharField()
	Addresse=forms.CharField()
class FormDescription(forms.Form):
	Name=forms.CharField()
	desc_text=forms.CharField()
class FormPortfolio(forms.Form):
	user=forms.CharField()
	Portfolio_name=forms.CharField()
	image=forms.ImageField()
	Type=forms.CharField()
	date=forms.DateField()
		
