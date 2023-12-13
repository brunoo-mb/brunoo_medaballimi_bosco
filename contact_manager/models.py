from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, unique = True)
    email = models.EmailField( unique = True )
    phone = models.CharField(max_length=15, blank=True, null=True)

    app_label = 'contact_manager'

    def __str__(self):
        return self.name
