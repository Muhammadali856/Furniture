from django.db import models
from common.models import BaseModel

class ContactModel(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'


