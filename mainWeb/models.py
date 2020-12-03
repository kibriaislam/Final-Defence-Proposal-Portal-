from django.db import models


class defenceInfo(models.Model):
    id = models.AutoField(primary_key=True)
    sId=models.CharField(max_length=1000)
    sName=models.CharField(max_length=1000)
    batch=models.CharField(max_length=1000)
    semester=models.CharField(max_length=1000)
    email=models.EmailField(max_length=1000)
    year=models.CharField(max_length=1000)
    pNumber=models.CharField(max_length=1000)
    defence=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.sName

    


# Create your models here.
