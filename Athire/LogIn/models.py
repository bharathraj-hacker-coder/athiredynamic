from django.db import models

# Create your models here.
class signin_credentials(models.Model):
    username= models.CharField(max_length=200, null=True)
    password= models.CharField(max_length=200, null=True)

    def __str__(self):
        return  self.username if self.username else ''

class dress_records(models.Model):
    dress_id = models.CharField(max_length=200, null=True)
    dress_name = models.CharField(max_length=200, null=True)
    cost = models.IntegerField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    dress_image = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.dress_id

class client_records(models.Model):
    order_id = models.CharField(max_length=200, null=True)
    client_name = models.CharField(max_length=200, null=True)
    client_location = models.CharField(max_length=200, null=True)
    shoot_date = models.DateField(max_length=200, null=True)
    coureir_date = models.DateField(max_length=200, null=True)
    return_date = models.DateField(max_length=200, null=True)
    booked_dress = models.CharField(max_length=200, null=True)
    payment_type = models.CharField(max_length=200, null=True)
    cost_details = models.CharField(max_length=200, null=True)
    received_date = models.DateField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.order_id
