from django.db import models

class Contact(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    email = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [created_on]

    def __str__(self):
        return f'{self.fname} {self.lname}'