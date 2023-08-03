from django.db import models

# Create your models here.
class ProjectModel(models.Model):
    project_name = models.CharField(max_length=15)
    project_description = models.CharField(max_length=50)
    project_lead = models.CharField(max_length=50)
    team_size = models.CharField(max_length=50)
    programming_language = models.CharField(max_length=50)
    project_start_date = models.DateField()
    project_delivery_date = models.DateField()