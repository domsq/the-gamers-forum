from django.db import models


class Contact(models.Model):
    """Schema for the Contact model, to be used for a contact form"""
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"Message {self.body} from {self.fname} {self.lname}"
