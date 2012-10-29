# -*- coding: UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Модель статьи
class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name=u'Название')
    url = models.CharField(max_length=300, verbose_name=u'URL', unique=True)
    desc = models.CharField(max_length=255, verbose_name=u'Описание')
    content = models.TextField(verbose_name=u'Текст')
    cat = models.ForeignKey('Category', verbose_name=u'Раздел', null=True, blank=True)

    def __unicode__(self):
        result = self.title
        return result


# Модель категории
class Category(MPTTModel):
    name = models.CharField(max_length=300, verbose_name=u'Название', unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        result = self.name
        return result
