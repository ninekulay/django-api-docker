from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Leave(models.Model):
    title = models.CharField(max_length=32,unique=True)
    description = models.TextField(max_length=255)
    
    def __str__(self):
        return self.title

class UserLeave(models.Model):
    leave = models.ForeignKey(Leave,on_delete=models.CASCADE)
    user_leave = models.FloatField(default='0',validators=[MinValueValidator(0.5)])
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user.username


