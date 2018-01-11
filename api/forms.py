from django import forms

from .models import DeliveryBookingModel

class DeliveryBookingForm(forms.Form):
    nom_expediteur= forms.CharField(max_length=100)
    adresse_ramassage = forms.CharField(max_length=200)
    telephone_expediteur = forms.CharField(max_length=20)
    nom_recepteur = forms.CharField(max_length=100)
    adresse_depot = forms.CharField(max_length=100)
    telephone_recepteur = forms.CharField(max_length=20)