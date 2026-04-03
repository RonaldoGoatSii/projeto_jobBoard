from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)  # Candidate
    is_employer = models.BooleanField(default=False)  # Company/Recruiter

    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    experience_years = models.IntegerField(default=0)

    def __str__(self):
        return self.username