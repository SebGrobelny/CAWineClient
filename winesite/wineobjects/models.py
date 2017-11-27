
# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Database models 
class Contact(models.Model):
    # __tablename__ = "contact"
    # id = models.Column(models.Integer, primary_key=True)
    name= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city =  models.CharField(max_length=200, default='')
    zipcode = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    single = models.CharField(max_length=200)
    multiple = models.CharField(max_length=200)
    looking = models.CharField(max_length=500)
    hear = models.CharField(max_length=500)
    time = models.DateTimeField(
         blank=True, null=True)

    #sumbission
    def submit(self):
        self.time = timezone.now()
        self.save()


    # def __repr__(self):
    #     return '<E-mail %r>' % self.email
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','time')

# Create our database model
class Request(models.Model):
    # __tablename__ = "request"

    # id = models.Column(models.Integer, primary_key=True)
    name= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city =  models.CharField(max_length=200, default='')
    zipcode = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    single = models.CharField(max_length=200)
    multiple = models.CharField(max_length=200)
    looking = models.CharField(max_length=500)
    hear = models.CharField(max_length=500)
    requestedwine = models.TextField()
    time = models.DateTimeField(
         blank=True, null=True)

    #sumbission
    def submit(self):
        self.time = timezone.now()
        self.save()


    # def __repr__(self):
    #     return '<E-mail %r>' % self.email
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','time','requestedwine')

class Inventory(models.Model):

	packaged = models.CharField(max_length=100)
	review_date = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	variety = models.CharField(max_length=100)
	lot = models.CharField(max_length=100)
	units = models.CharField(max_length=100)
	storage = models.CharField(max_length=100)
	year = models.CharField(max_length=100)
	ava = models.CharField(max_length=100)
	alc = models.CharField(max_length=100)
	chemanalysis = models.CharField(max_length=100)
	current = models.CharField(max_length=500)
	pending = models.CharField(max_length=500)
	other = models.CharField(max_length=500)
	promised = models.CharField(max_length=500)
	available = models.CharField(max_length=500)
	comments = models.CharField(max_length=500)

#admin view of inventory
# class InventoryAdmin(admin.ModelAdmin):
    # list_display = ('packaged','color','variety','lot','units','storage','year','ava','alc','chemanalysis','current','pending',
    #                 'other','promised','available','comments')
class InventoryResource(resources.ModelResource):

    class Meta:
        model = Inventory
        import_id_fields = ('id',)

class InventoryAdmin(ImportExportModelAdmin):
    resource_class = InventoryResource
    list_display = ('packaged','color','variety','lot','units','storage','year','ava','alc','chemanalysis','current','pending',
                    'other','promised','available','comments')
