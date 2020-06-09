from django.db import models
from datetime import datetime, timedelta
#from .tocsv import  modeltocsv
from django.core.management.base import BaseCommand, CommandError
import csv
import sys
from pytz import unicode

# Create your models here.
class Diseases(models.Model):
    CHOICES=(
        ('HI','Highly Infectious'),
        ('I','Infectious'),
        ('Nc','Not Communicable')
    )
    id = models.AutoField(primary_key = True)#added
    disease=models.CharField(max_length=50)
    symptoms=models.CharField(max_length=199)
    recoveryperiod=models.IntegerField(blank=True)#edited
    medications=models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField(null=True)
    CaseDate=models.DateField(auto_now=True)
    Expected_recovery_date=models.DateField(blank=True,null=True)
    threat_level=models.CharField(max_length=20,choices=CHOICES)
    

    def save(self, force_insert=False, force_update=False, *args, **kwargs):

        if self.recoveryperiod != "": # has error in timedelta function
            days=timedelta(days=self.recoveryperiod)
            print(days)
            self.Expected_recovery_date=datetime.now() + days
        super(Diseases, self).save(force_insert, force_update, *args, **kwargs)

        field_names = [f.name for f in Diseases._meta.fields]
        with open('data.csv','w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(field_names)
            for instance in Diseases.objects.all():
                writer.writerow([getattr(instance, f) for f in field_names])

        
    
     
    
                

class alert(models.Model):
    message=models.CharField(max_length=200)
    disease=models.CharField(max_length=30)
    symptoms=models.CharField(max_length=200)
    people_affected=models.IntegerField()
    people_recovered=models.IntegerField(blank=True)
    precautions=models.CharField(max_length=199,null=True,blank=True)


class symptoms(models.Model):
    id = models.AutoField(primary_key = True)
    symptom = models.TextField()

class question(models.Model):
    id = models.AutoField(primary_key = True)
    question = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.question

class answer(models.Model):
   
    ans = models.CharField(max_length = 10)
