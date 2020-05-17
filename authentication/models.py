from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    '''
    creating a manager for a custom user model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
    '''
    def create_user(self, email,phone,role,password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.phone=phone
        user.role=role
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.model(
            email=self.normalize_email(email),
        )
        
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self.db)
        return user

class CustomUser(AbstractBaseUser):

    CHOICES = (
        ('H', 'Hospital'),
        ('C', 'Clinic'),
    )
    role = models.CharField(max_length=10, choices=CHOICES)      
    phone = models.CharField(max_length=12, default = "")
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email 

    def is_admin(self):
        return self.is_superuser
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Hospital(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="hospital_account"
    )
    #new
    name = models.CharField(max_length=100,unique=True, null=True)
    registration_no = models.CharField(max_length=100,unique=True, null=True)
    address = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="clinic_account"
    )
    #new
    name = models.CharField(max_length=100,unique=True, null=True)
    registration_no = models.CharField(max_length=100,unique=True, null=True)
    address = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField(null=True)


    def __str__(self):
        return self.name
    

