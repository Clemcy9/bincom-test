from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone

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

    def __str__(self) -> str:
        return self.party_name

# polling unit > ward > lga > state : using this to define relationship amongs
# table

class State(models.Model):
    state_id = models.IntegerField(primary_key=True, unique=True)
    state_name = models.CharField(max_length=50, blank=False)

    def __str__(self) -> str:
        return self.state_name

class Lga(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    lga_id = models.IntegerField(max_length=11, blank=False)
    lga_name = models.CharField(max_length=50, blank=False)

    # 1 to many relationship with state 
    # state_id = models.IntegerField(max_length=50, blank=False)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateTimeField(default=timezone.now, blank=True,null=True)
    user_ip_address = models.GenericIPAddressField()

    def __str__(self) -> str:
        return self.lga_name

class Ward(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    ward_id = models.IntegerField(max_length=11, unique=False)
    ward_name = models.CharField(max_length=50, blank=False)
    # 1 to many relationship with lga
    lga_id = models.ForeignKey(Lga, on_delete=models.CASCADE, blank=True, null=True)
    ward_description = models.TextField(blank=True)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateTimeField(default=timezone.now, blank=True,null=True)

    def __str__(self) -> str:
        return self.ward_name

class Polling_unit(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    polling_unit_id = models.IntegerField(blank=False)
    # 1 to many relationship with ward
    ward_id = models.IntegerField(blank=True, null=True)
    # 1 to many with lga
    # lga_id = models.IntegerField()
    lga_id = models.ForeignKey(Lga, on_delete=models.CASCADE, blank=True, null=True)
    unique_ward_id = models.IntegerField(blank=True)
    polling_unit_number = models.CharField(max_length=50,blank=False)
    polling_unit_name = models.CharField(max_length=50, blank=False)
    polling_unit_description = models.TextField()
    lat = models.CharField(max_length=255, blank=True)
    long = models.CharField(max_length=255, blank=True)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateTimeField(default=timezone.now, blank=True,null=True)
    user_ip_address = models.GenericIPAddressField(null=True)

    def __str__(self) -> str:
        return self.polling_unit_name + ' PU'
    
class Announced_state_results(models.Model):
    state_name = models.CharField(max_length=50, blank=False)
    party_abbreviation = models.CharField(max_length=4, blank=False)
    party_score = models.IntegerField(max_length=11, blank=False)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateTimeField(default=timezone.now, blank=True,null=True)
    user_ip_address = models.GenericIPAddressField(null=True)

    def __str__(self) -> str:
        return self.state_name + 'announced result'

class Announced_lga_results(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)

    # 1 to many relationship
    # lga_name = models.ForeignKey(Lga, on_delete=models.CASCADE, blank=True, null=True)
    lga_name = models.CharField(max_length=50, blank=False, null=True)

    party_abbreviation = models.CharField(max_length=4, blank=False)
    party_score = models.IntegerField(blank=False)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateTimeField(default=timezone.now, blank=True,null=True)
    user_ip_address = models.GenericIPAddressField(null=True)

    def __str__(self) -> str:
        return self.lga_name + 'announced result'

class Announced_ward_results(models.Model):
    ward_name = models.CharField(max_length=50, blank=False)
    party_abbreviation = models.CharField(max_length=4, blank=False)
    party_score = models.IntegerField(max_length=11, blank=False)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateTimeField(default=timezone.now, blank=True,null=True)
    user_ip_address = models.GenericIPAddressField(null=True)

    def __str__(self) -> str:
        return self.ward_name + 'announced result'

class Announced_pu_results(models.Model):
    unique_id = models.IntegerField(primary_key=True, unique=True)
    polling_unit_uniqueid = models.CharField(max_length=50, blank=False)
    party_abbreviation = models.CharField(max_length=4, blank=False)
    party_score = models.IntegerField(max_length=11, blank=False)
    entered_by_user = models.CharField(max_length=50, blank=False)
    date_entered = models.DateTimeField(default=timezone.now, blank=True,null=True)
    user_ip_address = models.GenericIPAddressField(null=True)

    def __str__(self) -> str:
        return 'polling unit'+ self.polling_unit_uniqueid + 'announced result'
