from django.db import models


# Create your models here.
class Formalshirt(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)  


class Casualshirt(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
 
class Tshirt(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Trouser(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Jean(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Trackpant(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

