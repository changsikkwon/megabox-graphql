from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, account, phone_number, birth, name, password=None):
        if not email:
            raise ValueError("Email must be set!")
        user = self.model(
            email=email, account=account, phone_number=phone_number, birth=birth, name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, account):
        return self.get(account=account)


class User(AbstractBaseUser, TimeStampedModel):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    phone_number = models.CharField(max_length=20, unique=True)
    account = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.account

    objects = CustomUserManager()
    USERNAME_FIELD = "account"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    movie = models.ForeignKey("movie.Movie", on_delete=models.CASCADE, related_name="likes")

    class Meta:
        db_table = "like"
