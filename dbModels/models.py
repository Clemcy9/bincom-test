from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class Agent(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, blank=False)
    # pollingunit_uniqueid = models.UUIDField(default=str(uuid.uuid1())[:11], editable=False, unique=True)
    pollingunit_uniqueid = models.IntegerField(max_length=11,blank=False)

    REQUIRED_FIELDS = ['username','phone','pollingunit_uniqueid']
    USERNAME_FIELD = 'email'
    
    
    class Meta():
        # verbose_name ='Agent'
        verbose_name_plural = 'Agents'
    
    
    def __str__(self) -> str:
        return self.email

class Party(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    party_id = models.CharField(max_length=11, blank=False)
    party_name = models.CharField(max_length=11, blank=False)

# polling unit > ward > lga > state : using this to define relationship amongs
# table

class State(models.Model):
    state_id = models.IntegerField(primary_key=True, unique=True)
    state_name = models.CharField(max_length=50, blank=False)

class Lga(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    lga_id = models.IntegerField(max_length=11, blank=False)
    lga_name = models.CharField(max_length=50, blank=False)

    # 1 to many relationship with state 
    # state_id = models.IntegerField(max_length=50, blank=False)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateField(blank=False, auto_now_add=True)
    user_ip_address = models.GenericIPAddressField()

class Ward(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    ward_id = models.IntegerField(max_length=11, unique=True)
    ward_name = models.CharField(max_length=50, blank=False)
    # 1 to many relationship with lga
    lga_id = models.ForeignKey(Lga, on_delete=models.CASCADE, blank=True, null=True)
    ward_description = models.TextField(blank=True)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateField(blank=False, auto_now_add=True)

class Polling_unit(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    Polling_unit_id = models.IntegerField(blank=False)
    # 1 to many relationship with ward
    ward_id = models.IntegerField()
    # 1 to many with lga
    # lga_id = models.IntegerField()
    lga_id = models.ForeignKey(Lga, on_delete=models.CASCADE, blank=True, null=True)
    unique_ward_id = models.IntegerField(default=None)
    polling_unit_number = models.IntegerField(blank=False)
    polling_unit_name = models.CharField(max_length=50, blank=False)
    polling_unit_description = models.TextField()
    lat = models.CharField(max_length=255, blank=True)
    long = models.CharField(max_length=255, blank=True)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateField(blank=False, auto_now_add=True)
    user_ip_address = models.GenericIPAddressField()

class Announced_state_results(models.Model):
    state_name = models.CharField(max_length=50, blank=False)
    party_abbreviation = models.CharField(max_length=4, blank=False)
    party_score = models.IntegerField(max_length=11, blank=False)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateField(blank=False, auto_now_add=True)
    user_ip_address = models.GenericIPAddressField()

class Announced_lga_results(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    lga_name = models.CharField(max_length=50, blank=False)
    party_abbreviation = models.CharField(max_length=4, blank=False)
    party_score = models.IntegerField(blank=False)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateField(blank=False, auto_now_add=True)
    user_ip_address = models.GenericIPAddressField()

class Announced_ward_results(models.Model):
    ward_name = models.CharField(max_length=50, blank=False)
    party_abbreviation = models.CharField(max_length=4, blank=False)
    party_score = models.IntegerField(max_length=11, blank=False)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateField(blank=False, auto_now_add=True)
    user_ip_address = models.GenericIPAddressField()

class Announced_pu_results(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    polling_unit_uniqueid = models.CharField(max_length=50, blank=False)
    party_abbreviation = models.CharField(max_length=4, blank=False)
    party_score = models.IntegerField(max_length=11, blank=False)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateField(blank=False, auto_now_add=True)
    user_ip_address = models.GenericIPAddressField()
