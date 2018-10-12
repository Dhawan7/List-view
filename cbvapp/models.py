from django.db import models

class Collage(models.Model):
    name = models.CharField(max_length=250)
    principal_name = models.CharField(max_length=250)
    location = models.CharField(max_length=200)
    contact_no = models.PositiveIntegerField()
    registered_at = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
