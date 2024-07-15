from django.db import models

# Create your models here.

class User(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES ,null=True,default=None)
    
    def __str__(self):
        return self.email
        