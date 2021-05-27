from os import name
from django.db import models

# Create your models here.
class Candidate(models.Model):
    cand_name = models.CharField(max_length=25)
    cand_id = models.TextField()
    #id has to be auto generated later
    constituency = models.CharField(max_length=25)
    #add in vote symbol thumbnail later

    def __str__(self) -> str:
        return self.cand_name