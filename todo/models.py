from django.db import models
from django.utils import timezone   
import datetime

# Create your models here.

class ListWrapper(models.Model):
    listTitle = models.CharField(max_length=200)
    creationDate = models.DateTimeField('Created')

    def __str__(self):
        return self.listTitle

class ListItem(models.Model):
    listwrapper = models.ForeignKey(ListWrapper, on_delete=models.CASCADE)
    itemText = models.CharField(max_length=200)
    itemImportance = models.IntegerField(default=0)
    
    def __str__(self):
        return self.itemText + " importance = " + str(self.itemImportance)
