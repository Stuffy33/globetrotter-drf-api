from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    dress_code_choices = [
        ('beach_vibes', 'Beach Vibes'),
        ('casual', 'Casual'),
        ('button_up', 'Button up'),
        ('fancy', 'Fancy'),
    ]

    kids_friendly_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unknown', 'Unknown'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )

    dress_code = models.CharField(
        max_length=20,
        choices=dress_code_choices,
        default="none"
    )

    kids_friendly = models.CharField(
        max_length=20,
        choices=kids_friendly_choices,
        default="none"
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title}'