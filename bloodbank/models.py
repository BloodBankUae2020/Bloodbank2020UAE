from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Group(models.Model):
    bloodgroup = models.CharField(max_length=30)

    def __str__(self):
        return self.bloodgroup


class Donor(models.Model):
    fullname = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=15)
    emailid = models.CharField(max_length=50)
    gender = models.CharField(max_length=15)
    age = models.CharField(max_length=15)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, null=True)
    message = models.CharField(max_length=300, null=True)
    postingdate = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    donation_date = models.CharField(max_length=100)

    expiry_date = models.CharField(max_length=100)


    def __str__(self):
        return self.fullname + " " + self.group.bloodgroup


class Hospital(models.Model):

    HospitalName = models.CharField(max_length=100)
    ContactNo = models.CharField(max_length=15)
    Location = models.CharField(max_length=300, null=True)
    Aplus= models.CharField(max_length=10)
    Aminus = models.CharField(max_length=10)
    Bplus = models.CharField(max_length=10)
    Bminus = models.CharField(max_length=10)
    ABplus = models.CharField(max_length=10)
    ABminus = models.CharField(max_length=10)
    Oplus= models.CharField(max_length=10)
    Ominus = models.CharField(max_length=10)



    def __str__(self):
        return self.HospitalName + " " + self.Location


class Contact(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    emailid = models.CharField(max_length=40)
    message = models.CharField(max_length=300)
    mdate = models.DateField()
    isread = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    Email = models.EmailField()
    Context=models.CharField(max_length=300)
    Subject = models.CharField(max_length=100)

    def _str_(self):
        return self.Email




