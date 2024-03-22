from django.db import models

# Create your models here.

class Person(models.Model):
    Name=models.CharField(max_length=200,unique=True)
    Address=models.CharField(max_length=500)
    Mobileno=models.CharField(max_length=100)
    Bloodgrp=models.CharField(max_length=50)

    def __str__(self):
        return self.Name