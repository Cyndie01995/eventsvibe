from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Registration(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    attendance = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} attending {self.event.name}"    
