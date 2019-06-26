import uuid

from django.db import models
from django.urls import reverse


class ColorPalette(models.Model):
    one = models.CharField(max_length=18)
    two = models.CharField(max_length=18)
    three = models.CharField(max_length=18)
    four = models.CharField(max_length=18)
    five = models.CharField(max_length=18)
    six = models.CharField(max_length=18)
    seven = models.CharField(max_length=18)
    eight = models.CharField(max_length=18)
    nine = models.CharField(max_length=18)
    ten = models.CharField(max_length=18)


class Image(models.Model):
    image = models.ImageField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    top_colors = models.ForeignKey('ColorPalette', on_delete=models.CASCADE, blank=True)

    def get_absolute_url(self):
        return reverse("image_detail", kwargs={"pk": self.pk})
