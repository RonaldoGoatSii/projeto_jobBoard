from django.db import models

class JobListing(models.model):
    title =  models.CharField(max_lenght=50)
    level = models.CharField(max_lenght=20)
    salary_range = models.CharField(max_lenght=20)
    company = models.ForeignKey(on_delete=models.CASCADE)
    local = models.CharField(max_length=100)
    work = models.CharField(max_lenght=100)
    content = models.CharField(max_lenght=500)
    date_published = models.DateTimeField("date published")