from django.db import models
import os
import uuid
from shortuuidfield import ShortUUIDField
from django.db.models.signals import post_save

from userauths.models import User
from account.utils import create_new_ref_number,create_new_ref_pin

ACCOUNT_STATUS = (
    ("active", "Active"),
    ("pending", "Pending"),
    ("in-active", "In-active")
)

MARITAL_STATUS = (
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other")
)

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
)


IDENTITY_TYPE = (
    ("national_id_card", "National ID Card"),
    ("drivers_licence", "Drives Licence"),
    ("international_passport", "International Passport")
)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    ext = filename.split('.')[-1]
    filename = f"{instance.id}.{ext}"
    return f"user_{instance.id}/{filename}"

class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    #account_number = ShortUUIDField(unique=True,editable=False, max_length=25)
    account_number = models.CharField(max_length=10, unique=True, editable=False, default=create_new_ref_number)
    account_id = models.CharField(max_length=15, unique=True, editable=False, default=create_new_ref_number)
    pin_number = models.CharField(max_length=4,default=create_new_ref_pin)
    ref_code = ShortUUIDField(unique=True,editable=False,  max_length=25)
    account_status = models.CharField(max_length=10, choices=ACCOUNT_STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_approved = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="recommended_by")
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user}"
    
class KYC(models.Model):
    id = models.AutoField(primary_key=True,unique=True,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account= models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length = 255)
    image = models.ImageField(upload_to=user_directory_path,default='default.jpg')
    identity_image = models.ImageField(upload_to=user_directory_path,default='default.jpg')
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS)
    gender = models.CharField(choices=GENDER, max_length=25)  
    identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=35)
    date_of_birth = models.DateField()  
    signature = models.ImageField(upload_to=user_directory_path,default='default.jpg')  
    identity_number = models.CharField(max_length=255)

    # address
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    # contact
    mobile = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
         


    


def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

def save_account(sender, instance, **kwargs):
    instance.account.save()

post_save.connect(create_account, sender=User)
post_save.connect(save_account, sender=User)

       


