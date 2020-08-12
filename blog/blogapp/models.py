from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    #image = models.FileField(upload_to='media/', null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" %(self.id)

    class Meta:
        ordering = ["-id", "-timestamp"]
