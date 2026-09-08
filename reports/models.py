from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Report(models.Model):
     CATEGORIES = [
            ('document' ,'Document'),
            ('electronic','Electronic'),
            ('accesories','Accesories'),
            ('books','Books'),
            ('other','Other')
        ]
     STATUS_CHOICES = [
             ('active','Active'),
             ('resolved','Resolved')
         ]
     REPORT_TYPES= [
             ('lost','Lost'),
             ('found','Found')
         ]
       
     owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports'
        )
    
     item_name  = models.CharField(max_length=100)

     report_type = models.CharField(
          max_length=20,choices= REPORT_TYPES
          )
     
     category = models.CharField(
          max_length=20,choices=CATEGORIES
          )

   
     description = models.TextField()
     location = models.CharField(max_length=250)
     date = models.DateField()
     contact_info  = models.CharField(max_length=250)
     image = models.ImageField(
          upload_to='reports/',
          blank=True, 
          null=True
          )

     status = models.CharField(
          max_length=20, 
          choices=STATUS_CHOICES
          )
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.Item_name





    