from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """ Description: Category for Civil Civil Associations """
    name = models.CharField(max_length=50)

class Tag(models.Model):
    """ Description: Tags for AC's search """
    name = models.CharField(max_length=50)    

class CivilAssociation(models.Model):
    """ Description: Civil Association Model """
    name = models.CharField(max_length=255)
    founded_in = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    acronym = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    contact_email = models.EmailField(default='', blank=True)
    legal_representative = models.CharField(max_length=200, blank=True, default='')
    category = models.ForeignKey(Category)
    logo = models.ImageField(blank=True, null=True)
    facebook_url = models.CharField(max_length=255, default='', blank=True)
    twitter_url = models.CharField(max_length=255, default='', blank=True)
    instagram_url = models.CharField(max_length=255, default='', blank=True)
    tags = models.ManyToManyField(Tag)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified_on = models.DateTimeField(auto_now_add=True)

class BankAccount(models.Model):
    """ Description: Tags for AC's search """
    name = models.CharField(max_length=50)    
    account_number = models.CharField(max_length=50)    
    clabe = models.CharField(max_length=50)    
    branch_number = models.CharField(max_length=50)    
    bank_name = models.CharField(max_length=50)    
    civil_association = models.ForeignKey(CivilAssociation)
    
class MonetaryDonation(models.Model):
    """ Donacion Monetaria """
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User)
    donation_date = models.DateTimeField(auto_now_add=True)
    bank_account = models.ForeignKey(BankAccount)
    civil_association = models.ForeignKey(CivilAssociation)

class VolunteeringPledge(models.Model):
    """ Para voluntarios """
    user = models.ForeignKey(User)
    donation_date = models.DateTimeField(auto_now_add=True)
    bank_account = models.ForeignKey(BankAccount)
    civil_association = models.ForeignKey(CivilAssociation)    