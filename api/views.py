from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import requests
import json


from .forms import DeliveryBookingForm
from .serializers import DeliveryBookingSerializer


def save_delivery_order(request):

    if request.method == "POST":
        form = DeliveryBookingForm(request.POST)
        if form.is_valid():
            nom_expediteur = form.cleaned_data['nom_expediteur']
            adresse_ramassage = form.cleaned_data['adresse_ramassage']
            telephone_expediteur = form.cleaned_data['telephone_expediteur']
            nom_recepteur = form.cleaned_data['nom_recepteur']
            adresse_depot = form.cleaned_data['adresse_depot']
            telephone_recepteur = form.cleaned_data['telephone_recepteur']

            post_data={
                "apiKey": settings.GETSWIFT_API_KEY,
                "booking":{
                    "pickupDetail": {
                        "name": nom_expediteur,
                        "phone": telephone_expediteur,
                        "address": adresse_ramassage
                    },
                    "dropoffDetail": {
                        "name": nom_recepteur,
                        "phone": telephone_recepteur,
                        "address": adresse_depot
                    }
                }
            }

            headers={'content-type': 'application/json'}
            url = 'https://app.getswift.co/api/v2/deliveries'
            r = requests.post(url, headers=headers, data=json.dumps(post_data))
            print(r)
            # print(r.text)
            # return HttpResponse(r.status_code)
            json_data = r.json()
            serializer = DeliveryBookingSerializer(data=json_data)
            print (serializer)
            if serializer.is_valid():
                info = serializer.save()
                return render(request, 'info.html', {'info': info})
            else:
                return HttpResponse("Serializer not valid")
    else:
        form = DeliveryBookingForm()

    return render(request, 'form.html', {'form': form})
