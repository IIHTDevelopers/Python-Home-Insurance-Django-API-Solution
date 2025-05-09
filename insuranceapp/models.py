from django.db import models

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

class QuoteModel(models.Model):
    quote_id = models.AutoField(primary_key=True)
    user_id=models.IntegerField()
    hno=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    residance_type= models.CharField(max_length=50)
    residance_use= models.CharField(max_length=100)
    detached_structure = models.CharField(max_length=100)
    market_value=models.DecimalField(decimal_places=2,max_digits=100)
    year_build=models.IntegerField()
    square_foot_value=models.IntegerField()
    dwelling_style= models.CharField(max_length=50)
    roof_material= models.CharField(max_length=50)
    garage_type= models.CharField(max_length=50)
    numfullBaths=models.IntegerField()
    numhalfBaths=models.IntegerField()
    has_swimming_pool=models.BooleanField(default=False)

class PolicyModel(models.Model):
    policy_key= models.AutoField(primary_key=True)
    quote_id= models.IntegerField()
    policy_term = models.CharField(max_length=20)
    policy_effective_date=models.DateField()
    policy_end_date=models.DateField()
    status= models.CharField(max_length=50,default="None")


# class ResidanceModel(models.Model):
#     residance_type= models.CharField(max_length=50)
#     address_line1= models.CharField(max_length=100)
#     address_line2= models.CharField(max_length=100)
#     city= models.CharField(max_length=50)
#     residance_use= models.CharField(max_length=100)
#     user_name = models.CharField(max_length=50)
#
#
# class PropertyModel(models.Model):
#     quote_id= models.IntegerField()
#     user_id=models.IntegerField(primary_key=True)
#     market_value=models.DecimalField(decimal_places=2,max_digits=100)
#     year_build=models.IntegerField()
#     square_foot_value=models.IntegerField()
#     dwelling_style= models.CharField(max_length=50)
#     roof_material= models.CharField(max_length=50)
#     garage_type= models.CharField(max_length=50)
#     numfullBaths=models.IntegerField()
#     numhalfBaths=models.IntegerField()
#     has_swimming_pool=models.BooleanField(default=False)
