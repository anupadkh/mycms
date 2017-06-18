# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Personal
# Register your models here.
# admin.site.register(Personal)
# admin.site.register(Family)

'''
doesn't works
a = [Personal, Address, Nagrikta, Contact, Media, Hobby]
for classed in a:
    admin.site.register(classed)
'''

from django.apps import apps

app = apps.get_app_config('personal')

for model_name, model in app.models.items():
    admin.site.register(model)
