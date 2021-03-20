from django.db import models
from user.models import TimeStampedModel
from django.utils.translation import gettext as _

IMAGE_MAIN = 1
IMAGE_SUB = 2
IMAGES = 3

IMAGE_CHOICES = (
    (IMAGE_MAIN, (_("메인이미지"))),
    (IMAGE_SUB, (_("서브이미지"))),
    (IMAGES, (_("나머지이미지"))),
)


class Movie(TimeStampedModel):
    title = models.CharField(max_length=100)
    english_title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    opening_date = models.DateField(null=True, blank=True)
    running_time = models.PositiveIntegerField(null=True, blank=True)
    ticketing_rate = models.DecimalField(
        max_digits=3, decimal_places=1, default=0.0, null=True, blank=True
    )
    audience_rating = models.ForeignKey("AudienceRating", on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey("Tag", on_delete=models.SET_NULL, null=True, default=None)
    actor = models.ManyToManyField("Actor")
    director = models.ManyToManyField("Director")
    genre = models.ManyToManyField("Genre")
    type = models.ManyToManyField("Type")

    class Meta:
        db_table = "movie"
        ordering = (
            "-ticketing_rate",
            "title",
        )

    def __str__(self):
        return self.title


class Image(TimeStampedModel):
    movie = models.ForeignKey(Movie, related_name="images", on_delete=models.CASCADE)
    url = models.URLField()
    type = models.PositiveSmallIntegerField(choices=IMAGE_CHOICES)

    class Meta:
        db_table = "image"


class Rating(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    class Meta:
        db_table = "rating"


class AudienceRating(models.Model):
    grade = models.CharField(max_length=20)

    class Meta:
        db_table = "audience_rating"


class Tag(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = "tag"


class Actor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "actor"


class Director(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "director"


class Genre(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "genre"


class Type(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "type"
