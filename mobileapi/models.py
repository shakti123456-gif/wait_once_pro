from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, mobile_number, first_name, last_name, Dateofbirth, email_address=None, ndis_number=None, password=None):
        if not mobile_number:
            raise ValueError('Users must have a mobile number')
        
        user = self.model(
            mobile_number=mobile_number,
            first_name=first_name,
            last_name=last_name,
            Dateofbirth=Dateofbirth,
            email_address=email_address,
            ndis_number=ndis_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, first_name, last_name, Dateofbirth, email_address=None, ndis_number=None, password=None):
        user = self.create_user(
            mobile_number,
            first_name=first_name,
            last_name=last_name,
            Dateofbirth=Dateofbirth,
            email_address=email_address,
            ndis_number=ndis_number,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User_mobile(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Dateofbirth = models.DateField()
    mobile_number = models.CharField(max_length=15, unique=True)
    email_address = models.CharField(max_length=100, null=True, blank=True)
    ndis_number = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    #  is_admin = models.BooleanField(default=False)
    password=models.CharField(max_length=15)

    objects = UserManager()

    USERNAME_FIELD = 'mobile_number'
    # REQUIRED_FIELDS = ['first_name', 'last_name', 'Dateofbirth']

    class Meta:
        # db_table = 'Mobile_user'
        pass

    def __str__(self):
        return self.mobile_number

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def check_password(self, raw_password):
        return self.password==raw_password



class CustomerDetails(models.Model):
    height = models.CharField(max_length=5,null=True,blank=True)
    weight = models.CharField(max_length=5,null=True,blank=True)
    medical_history=models.TextField(null=True,blank=True)
    documents=models.FileField(null=True,blank=True)
    data_user = models.ForeignKey('User_mobile', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'CustomerDetails'
        verbose_name_plural = 'CustomerDetails'
        ordering = ['id']
        # db_table = 'mobileapi_customerdetails'
        # managed=False

    

class SubUser(models.Model):
    sub_user_id = models.AutoField(primary_key=True)
    parent_detail = models.ForeignKey('User_mobile', null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    ndis_number=models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'Subuser'
        verbose_name_plural = 'Subuser'
        ordering = ['sub_user_id']
        # db_table = 'mobileapi_subuser'
        # managed=False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'
        ordering = ['service_id']
        # db_table = 'mobileapi_service'

    def __str__(self):
        return self.name

class Therapist(models.Model):
    therapist_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Bio=models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'Therapist'
        verbose_name_plural = 'Tharapists'
        ordering = ['therapist_id']
        # db_table = 'mobileapi_therapist'
        # managed = False


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Apointment(models.Model):
    User_mobile=models.ForeignKey('User_mobile', null=True, on_delete=models.SET_NULL)
    Apointment_id=models.AutoField(primary_key=True)
    Unique_id=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True)
    Booked=models.BooleanField(default=True)

    # class meta:
    #     db_table = 'Mobile_user'

    

class Provider(models.Model):
    Provider_id = models.AutoField(primary_key=True)
    organization_name=models.CharField(max_length=100)
    Therapist_add=models.ManyToManyField(Therapist,blank=True)
    services = models.ManyToManyField(Service, related_name='therapy', blank=True)
    Apointment=models.ManyToManyField(Apointment,blank=True)
    def __str__(self):
        return f"{self.organization_name}"

    class meta:
        db_table = 'mobileapi_provider'
        # managed = False



