from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

TIME_SLOT = (
    ("9:00 - 10:00", "9:00 - 10:00"),
    ("10:00 - 11:00", "10:00 - 11:00"),
    ("11:00 - 12:00", "11:00 - 12:00"),
    ("14:00 - 15:00", "14:00 - 15:00"),
    ("15:00 - 16:00", "15:00 - 16:00"),
    ("16:00 - 17:00", "16:00 - 17:00"),
    ("17:00 - 18:00", "17:00 - 18:00"),
    ("20:00 - 21:00", "20:00 - 21:00"),
    )
STATUS = ((0, "Draft"), (1, "Published"))


class YogaClass(models.Model):
    yoga_type = models.CharField(
        max_length=90, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    available_spaces = models.IntegerField(default=20)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.yoga_type


class Reservation(models.Model):
    yoga_class = models.ForeignKey(
        YogaClass, on_delete=models.CASCADE, related_name="chosen_class"
    )
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="member"
    )
    name = models.CharField(max_length=80, null=False, blank=False)
    surname = models.CharField(max_length=80, null=False, blank=False)
    day = models.DateField(null=False, blank=False)
    time = models.CharField(
        max_length=15, choices=TIME_SLOT, default="9:00 - 10:00", null=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation: {self.day}, {self.time} {self.yoga_class}"
        f"by {self.name} {self.surname}"
