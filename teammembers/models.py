from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=60)
    job_title = models.CharField(max_length=60)

    def __str__(self):
        return self.name