from django.db import models
from django.contrib.auth.models import User

class photos(models.Model):
    published_date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    caption = models.TextField()
    photo = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    draft = models.BooleanField(default=False)

    def __str__(self) :
        return self.caption
