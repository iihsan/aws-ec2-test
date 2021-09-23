from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from .manager import UserManager

class User(AbstractUser):
  username = None
  email = models.EmailField(unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  def __str__(self):
      return self.email