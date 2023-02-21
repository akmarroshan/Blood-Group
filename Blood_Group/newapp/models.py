from django.db import models
class QuesModel(models.Model):
    
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    userrecommend=models.CharField(max_length=100)
    prefer=models.CharField(max_length=100)
    Comment=models.CharField(max_length=150)

class loginmodel(models.Model):

    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
class Signupmodel(models.Model):

    email=models.CharField(max_length=100)
    psw=models.CharField(max_length=100)
    pswrepeat=models.CharField(max_length=100)
    # remember=models.CharField(max_length=100)

class attendmodel(models.Model):
    # Empcode=models.CharField(max_length=100)
    Empname=models.CharField(max_length=100)
    drpleavetypele=models.CharField(max_length=100)
    drpapplyingtyp=models.CharField(max_length=100)
    Noofdays=models.IntegerField()
    todate=models.CharField(max_length=150)
    fromdate=models.CharField(max_length=150)
    mobileno=models.CharField(max_length=150)
    status=models.CharField(max_length=150,default="Waiting")