from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    """ Model for representing message object """

    content = models.TextField(max_length=250)
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content


class MessageImage(models.Model):
    """ Model for representing images of the message  """

    image = models.ImageField(upload_to="images")
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url
