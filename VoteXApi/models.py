# reference from labs1-4
from datetime import timedelta, datetime
from enum import Enum

from django.db import models
from multiselectfield import MultiSelectField


class Region(Enum):
    VINNYTSIA = 'vinnytsia'
    VOLYN = 'volyn'
    DNIPROPETROVSK = 'dnipropetrovsk'
    DONETSK = 'donetsk'
    ZHYTOMYR = 'zhytomyr'
    ZAKARPATTIA = 'zakarpattia'
    ZAPORIZHZHIA = 'zaporizhzhia'
    IVANO_FRANKIVSK = 'ivano-frankivsk'
    KYIV = 'kyiv'
    KIROVOHRAD = 'kirovohrad'
    LUHANSK = 'luhansk'
    LVIV = 'lviv'
    MYKOLAIV = 'mykolaiv'
    ODESA = 'odesa'
    POLTAVA = 'poltava'
    RIVNE = 'rivne'
    SUMY = 'sumy'
    TERNOPIL = 'ternopil'
    KHARKIV = 'kharkiv'
    KHERSON = 'kherson'
    KHMELNYTSKYI = 'khmelnytskyi'
    CHERKASY = 'cherkasy'
    CHERNIVTSI = 'chernivtsi'
    CHERNIHIV = 'chernihiv'

    def __str__(self):
        return self.value


class Organization(Enum):
    SOFTSERVE = 'softserve'
    GOOGLE = 'google'
    BING = 'bing'

    def __str__(self):
        return self.value


class Role(Enum):
    ADMIN = 'admin'
    VOTER = 'voter'

    def __str__(self):
        return self.value


#
#
# # Create your models here.
# General model for any user
class User(models.Model):
    email = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=120, unique=True, null=True)
    password = models.CharField(max_length=45)
    register_date = models.DateTimeField(auto_now_add=True)
    region = models.CharField(
        max_length=45,
        choices=[(region.name, region.value) for region in Region],
        null=True
    )
    organization = models.CharField(
        max_length=45,
        choices=[(organization.name, organization.value) for organization in Organization],
        null=True
    )
    role = models.CharField(
        max_length=45,
        choices=[(role.name, role.value) for role in Role],
        null=True
    )

    def __str__(self):
        return self.email


class Election(models.Model):
    name = models.CharField(max_length=120)
    votes_per_voter = models.IntegerField()
    retractable_votes = models.BooleanField(default=False)
    anonymous = models.BooleanField(default=True)
    start_of_voting = models.DateTimeField(auto_now_add=True)
    end_of_voting = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    organizations = models.CharField(
        max_length=45,
        choices=[(organization.name, organization.value) for organization in Organization],
    )
    regions = MultiSelectField(
        max_length=45,
        choices=[(region.name, region.value) for region in Region],
    )
    role = models.CharField(
        max_length=45,
        choices=[(role.name, role.value) for role in Role],
    )

    def __str__(self):
        return self.name

#
#
# class Pax(models.Model):
#     user = models.OneToOneField("User", on_delete=models.CASCADE)
#     name = models.CharField(max_length=45)
#     phone_number = models.CharField(max_length=45)
#     card_info = models.CharField(max_length=45)
#
#     def __str__(self):
#         return self.name
#
#
# class Driver(models.Model):
#     user = models.OneToOneField("User", on_delete=models.CASCADE)
#     name = models.CharField(max_length=45)
#     car_name = models.CharField(max_length=45)
#     rating = models.FloatField()
#     phone_number = models.CharField(max_length=45)
#     card_info = models.CharField(max_length=45)
#
#     def __str__(self):
#         return self.name
#
#
# class Ride(models.Model):
#     pax = models.ForeignKey("Pax", on_delete=models.CASCADE)
#     driver = models.ForeignKey("Driver", on_delete=models.CASCADE)
#     start_gps = models.CharField(max_length=45, default=0)
#     end_gps = models.CharField(max_length=45, default=0)
#     payment_method = models.CharField(max_length=45)
#     stars = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.driver.name
# # python manage.py makemigrations
# # python manage.py migrate
