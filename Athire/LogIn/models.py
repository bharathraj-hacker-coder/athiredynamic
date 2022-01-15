from django.db import models

# Create your models here.
class signin_credentials(models.Model):
    username= models.CharField(max_length=200, null=True)
    password= models.CharField(max_length=200, null=True)

    def __str__(self):
        return  self.username if self.username else ''