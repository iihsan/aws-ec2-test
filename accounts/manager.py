from django.contrib.auth.models import BaseUserManager
# from django.core.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager as AbstractUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password=None,is_active=True,is_staff=False,is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.superuser = True
        user.save(using=self._db)
        return user

# class UserManager(AbstractUserManager):
#   def create_user(self, email, password, **extra_fields):
#     if not email:
#       raise ValueError("Email must be set")

#     email = self.normalize_email(email)
#     user = self.model(email=email, **extra_fields)
#     user.set_password(password)
#     user.save()
#     return user

# def create_superuser(self, email, password, **extra_fields):
#     extra_fields.setdefault('is_staff', True)
#     extra_fields.setdefault('is_active', True)
#     extra_fields.setdefault('is_superuser', True)

#     if extra_fields.get('is_staff') is not True:
#         raise ValueError('Superuser must be a staff')
    
#     if extra_fields.get('is_superuser') is not True:
#         raise ValueError('Superuser flag must be true')
    
#     return self.create_user(email=email, password=password, **extra_fields)