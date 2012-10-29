# -*- coding: UTF-8 -*-
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import Article
from models import Category

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Article)
