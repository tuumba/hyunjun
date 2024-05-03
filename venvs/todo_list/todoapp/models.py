from django.db import models

# Create your models here.

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    modify_date = models.DateTimeField(null=True,blank=True)
    completed = models.BooleanField(default= False)