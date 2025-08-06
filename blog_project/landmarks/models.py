from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Landmark(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='landmarkdata', null=True)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField(blank=True)
    landmark= models.ForeignKey(Landmark, on_delete=models.CASCADE, related_name='comments')
    file = models.FileField(upload_to='userdata' ,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class PickTheme(models.Model):
    themes = (
        ('Light Mode', 'light'),
        ('Dark Mode', 'dark'),
    )
    picktheme_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.CharField(max_length=255, choices=themes)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user'], name='One Entry Per User')
        ]