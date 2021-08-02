from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom User Manager for User Model in authmk/models.py/User
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        for custom create normal user by email and password
        :param email: email is USERNAME_FIELD and REQUIRED_FIELDS
        :param password: password user
        :return: create user with is_staff = is_superuser = False
        """
        if not email:
            raise ValueError('Email field is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        for custom create superuser by email and password
        :param email: email is USERNAME_FIELD and REQUIRED_FIELDS
        :param password: password superuser
        :param extra_fields: other fields for example = is_staff, is_superuser, is_active, name
        :return: create superuser with is_staff = is_superuser = True
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('name', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')

        return self.create_user(email=email, password=password, **extra_fields)
