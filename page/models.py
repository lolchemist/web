#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
#User = get_user_model()

class Person(User):
    first_name = models.CharField(max_length=255, verbose_name = 'Имя')#first name
    last_name = models.CharField(max_length=255, verbose_name = 'Фамилия')
    weigth =  models.FloatField(verbose_name = 'Вес', blank = True)
    heigth = models.FloatField(verbose_name = 'Рост', blank = True)
    mail = models.EmailField(max_length = 255, blank = True)
    description = models.TextField(blank = True)
#image = models.ImageField(upload_to = 'photos', blank = True)
    sex = models.CharField(max_length=1, choices = (
                                                    ('F', 'Female'),
                                                    ('M', 'Male')
                                                    ), null = True)
    age = models.PositiveIntegerField(null = True)
        
    def __str__(self):
                    return self.first_name + ' ' + self.last_name
#    activity = models.OneToManyField(to = activity, blank = True)
        
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['surname']

class Product(models.Model):
    name =  models.CharField(max_length=255, verbose_name = 'Продукт')
    prod_ccal = models.FloatField(verbose_name = 'Калорийность продукта')
    prod_weigth = models.FloatField(verbose_name = 'Вес продукта')
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=255, verbose_name = 'Блюдо')
    ingredients =  models.ManyToManyField(to = Product)
    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_legth= 255, verbose_name = 'Занятие')
    activity_time = models.DurationField(verbose_name = 'Длительность')
    ccals = models.IntegerField(verbose_name = 'ккал/час')
    def __str__(self):
        return self.name


class Activity(models.Model):
    description = models.TextField()
    add_time = models.DateTimeField(unique_for_date="add_time",auto_now = True, verbose_name = 'Активность')
    food = models.ManyToManyField(to=Food)
    training = models.ManyToManyField(to = Workout)
    person = models.ForeignKey(to = Person)
    def __str__(self):
        return self.name
    class Meta:
        get_latest_by = "add_time"
        verbose_name = "Физическая активность"
        verbose_name_plural = "Активности"

class Like(models.Model):
    who = models.ForeignKey(to = Person)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        index_together = [["content_type", "object_id"],]
                        

# Create your models here.
