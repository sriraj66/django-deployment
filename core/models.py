from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=5)
    roll = models.CharField(max_length=5)
    profile = models.ImageField(upload_to="Profile/",blank=True)
    
    def __str__(self) -> str:
        return self.name