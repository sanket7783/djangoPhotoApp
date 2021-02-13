from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validateImage(image):
    #import pdb; pdb.set_trace()
    imgSize = image.size
    limit_kb = 15000
    limit_height = 200
    limit_width = 200
    if limit_height < image.image.height:
        raise ValidationError("Max size of file is %s " % limit_height)
    if limit_width < image.image.width:
        raise ValidationError("Max size of file is %s " % limit_width)
    if imgSize > limit_kb*1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)

class photos(models.Model):
    published_date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    caption = models.TextField()
    photo = models.ImageField(upload_to='images/',validators=[validateImage])
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    draft = models.BooleanField(default=False)

    def __str__(self) :
        return self.caption
