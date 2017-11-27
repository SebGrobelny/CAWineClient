# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect, HttpResponse

import json
from collections import OrderedDict

from .models import Inventory,Contact, Request

from datetime import datetime
from pytz import timezone

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact(request):
	#check to see if method is post
	if request.method == "POST":

		data = request.POST

		new_contact = Contact(  name=str(data['first'])+" "+str(data['last']), email=data['email'], 
					    phone=data['phone'], address1=data['address1'], address2=data['address2'],
					    city=data['city'],zipcode=data['zip'], state=data['state'], country=data['country'],
					    single=data['single'], multiple=data['multiple'], looking = data['usrform'],
					    hear=data['usrform1'])

		time = str(datetime.now(timezone('US/Pacific')))
		time = time.split(".")[0]
		new_contact.time = time

		new_contact.save()
		
		return HttpResponseRedirect("https://californiawineclassics.com/home")

    #otherwise restrict access
	else:

		return HttpResponse(status=404)


#view that interacts with DB
@csrf_exempt
def still_wine(request):
	#use  QuerySet to obtain the desired filters
	status_code = 200

	if request.method == "POST":
		data = request.POST
		request_data = request.POST.getlist('request')

		request_data = request_data[0].split(",")

		for request in request_data:
			wine = Inventory.objects.filter(id=int(request)).get()


			new_request = Request(  name=str(data['first'])+" "+str(data['last']), email=data['email'], 
								    phone=data['phone'], address1=data['address1'], address2=data['address2'],
								    city=data['city'],zipcode=data['zip'], state=data['state'], country=data['country'],
								    single=data['single'], multiple=data['multiple'], looking = data['usrform'],
								    hear=data['usrform1'])

			new_request.requestedwine = str(wine.variety)+" "+str(wine.ava)+" "+str(wine.year)+" "+str(wine.current)+" "+str(wine.units)+" "+str(wine.lot)+" "+str(wine.comments)

			time = str(datetime.now(timezone('US/Pacific')))
			time = time.split(".")[0]


			new_request.time = time
			new_request.save()

		return HttpResponseRedirect("https://californiawineclassics.com/home")

	else:
		reds = Inventory.objects.filter(color='Red')
		whites = Inventory.objects.filter(color='White')
		# form = RequestForm()
		redList = []

		for red in reds:

			element = OrderedDict()

			element['0Red'] = red.id
			element['1Variety']= red.variety
			element['2AVA'] = red.ava
			element['3Year'] = red.year
			element['4Inventory'] = red.current
			element['5Units'] = red.units
			element['6Lot'] = red.lot
			element['7Comments'] = red.comments

			redList.append(element)

		whiteList = []
		for white in whites:
			element = OrderedDict()

			element['0White'] = white.id
			element['1Variety']= white.variety
			element['2AVA'] = white.ava
			element['3Year'] = white.year
			element['4Inventory'] = white.current
			element['5Units'] = white.units
			element['6Lot'] = white.lot
			element['7Comments'] = white.comments

			whiteList.append(element)


		body = {'reds': redList, 'white':whiteList}

	return HttpResponse(content= json.dumps(body), status=status_code, content_type="application/json")