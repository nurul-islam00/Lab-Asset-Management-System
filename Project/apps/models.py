from django.db import models
class student(models.Model):
    id=models.CharField(max_length=50,blank=False,primary_key=True)
    email=models.EmailField(max_length=50,blank=False)
    name=models.CharField(max_length=50,blank=False)
    batch=models.CharField(max_length=50,blank=False)
    code=models.CharField(max_length=50,blank=False)
    hall=models.CharField(max_length=50,blank=False)

class instrument(models.Model):
     id=models.CharField(max_length=50,blank=False,primary_key=True)
     name=models.CharField(max_length=50,blank=False)
     price=models.IntegerField(blank=False)
     ins_type=models.CharField(max_length=50,blank=True)
     status=models.CharField(max_length=50,blank=False)


class assign(models.Model):
    ins_id = models.CharField(max_length=50,primary_key=True)
    regi_id=models.CharField(max_length=50)
   
