from django.db import models

# Create your models here.
class Diseases(models.Model):
    disease=models.CharField(max_length=50)
    symptoms=models.CharField(max_lenth=199)
    recoveryperiod=models.IntegerField()
    medications=models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField(null=True)
    

