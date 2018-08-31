from django.db import models
from uuid import uuid4

# Create your models here.
class Notes(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    last_modified= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural= "notes"