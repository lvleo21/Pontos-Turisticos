from django.db import models

class Atracao(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    minimum_age = models.IntegerField()
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]