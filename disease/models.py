from django.db import models
from datetime import datetime, timedelta

from .tocsv import  modeltocsv


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
    #Expected_recovery_date=models.DateTimeField(blank=True)
    threat_level=models.CharField(max_length=20,choices=CHOICES)
    

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.recoveryperiod:# has error in timedelta function
            days=timedelta(days=self.recoveryperiod)
            self.Expected_recovery_date=self.CaseDate + days
        super(Diseases, self).save(force_insert, force_update, *args, **kwargs)

        objects = Diseases.objects.all()
        field = Diseases._meta.fields

        print (field)#to check
        modeltocsv(objects, field)

        
    
     
    
                

class alert(models.Model):
    message=models.CharField(max_length=200)
    disease=models.CharField(max_length=30)
    symptoms=models.CharField(max_length=200)
    people_affected=models.IntegerField()
    people_recovered=models.IntegerField(blank=True)