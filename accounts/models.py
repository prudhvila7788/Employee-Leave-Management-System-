from django.db import models
from django.contrib.auth.models import User

class EmployeeDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    # Add any other fields you need for EmployeeDetails

    def __str__(self):
        return self.name

