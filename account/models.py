from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password=None, **other_fields):
        if not email:
            raise ValueError('User enter a valid email address')
        elif not username:
            raise ValueError('User must enter a username')
        user = self.model(
                email=self.normalize_email(email),
                username=username,
                **other_fields
            )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    username        = models.CharField(max_length=150, unique=True)
    email           = models.EmailField(verbose_name='email', max_length=254, unique=True)
    department      = models.CharField(verbose_name='department', max_length=100, editable=True)
    first_name      = models.CharField(verbose_name='first name', max_length=254, blank=True)
    last_name       = models.CharField(verbose_name='last name', max_length=254, blank=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']
    objects = MyAccountManager()

    class Meta:
        verbose_name_plural = "Account"
        ordering            = ['-date_joined']
    
    def __str__(self):
        return self.username
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

# class Profile(models.Model):
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#     department = models.CharField(max_length=100)
#     def __str__(self):
#         return str(self.user.username + " " + self.department)
