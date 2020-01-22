# -*- coding: utf-8 -*-
from django.db import models
from django import forms

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    month = forms.CharField()
