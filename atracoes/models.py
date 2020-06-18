from django.db import models

class Atracao(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    minimum_age = models.IntegerField()
    foto = models.ImageField(upload_to="atracoes", null=True, blank=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]