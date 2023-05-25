# reference from labs1-4

from django.db import models


#
#
# # Create your models here.
#
class User(models.Model):
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
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
