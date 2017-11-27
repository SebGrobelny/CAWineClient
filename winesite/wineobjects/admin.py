# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#import export
from import_export import resources

#models and their admin views
from .models import Request, RequestAdmin
from .models import Contact , ContactAdmin
from .models import Inventory , InventoryAdmin

#configuration for importing and exporting
class InventoryResource(resources.ModelResource):

    class Meta:
        model = Inventory

class ContactResource(resources.ModelResource):

    class Meta:
        model = Contact

class RequestResource(resources.ModelResource):

    class Meta:
        model = Request

# Register your models here.
admin.site.register(Request, RequestAdmin)

admin.site.register(Contact, ContactAdmin)

admin.site.register(Inventory, InventoryAdmin)



