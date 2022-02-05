from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=60)
    created = created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name