from django.db import models

class enquiry_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name
    
    
# Create your models here.
