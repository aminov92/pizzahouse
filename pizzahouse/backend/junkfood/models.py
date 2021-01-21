from django.db import models

# Create your models here.
class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=250)

class Menus(models.Model):
    menu_id = models.AutoField(primary_key=True)
    meny_img=models.ImageField()
    menu_name = models.CharField(max_length=250)
    menu_body = models.TextField()

class Profiles(models.Model):
    profile_id = models.AutoField(primary_key=True)
    profile_firstname= models.CharField(max_length=250)
    profile_lasttname= models.CharField(max_length=250)
    profile_pseudo= models.CharField(max_length=250)
    profile_password= models.CharField(max_length=250)

class Supplements(models.Model):
    supplement_id = models.AutoField(primary_key=True)
    supplement_name = models.CharField(max_length=250)

def str(self):
        return self.name

