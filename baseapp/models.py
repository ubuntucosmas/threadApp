from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#===================================================================================================================
class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#===================================================================================================================

class Thread(models.Model):
    host= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) #null set to True in the database
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # participants =
    updated = models.DateTimeField(auto_now=True) #takes a snashop of the time every time it is updated
    created = models.DateTimeField(auto_now_add=True) #takes a snashop of the time when it was created
    topic_image = models.ImageField(null=True, blank=True,upload_to='images/')

    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.name
    
#===================================================================================================================
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True) #takes a snashop of the time every time
    created = models.DateTimeField(auto_now_add=True) #takes a snashop of the time when
    def __str__(self):
        return self.content[0:50] # trim to only the first 50 characters[0:50]
    

