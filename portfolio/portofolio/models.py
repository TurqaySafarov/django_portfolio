
from django.db import models

class Portfolio(models.Model):
    ad = models.CharField(max_length=150)  
    soyad = models.CharField(max_length=150)    
    ata_adı = models.CharField(max_length=150)  
    doğum_tarixi = models.DateField()
    doğum_yeri = models.CharField(max_length=150)  
    cinsiyyət = models.CharField(max_length=10)  
    aile_vəziyyəti = models.CharField(max_length=50) 
    əlaqə_nömrəsi = models.CharField(max_length=15) 
    email = models.EmailField()
    yaşayış_yeri = models.CharField(max_length=200)  
    təhsil = models.CharField(max_length=200) 
