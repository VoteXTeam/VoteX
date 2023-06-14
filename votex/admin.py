from django.contrib import admin

# Register your models here.
from .models import GlobalElection, LocalElection, Candidate, Location, Voter

admin.site.register(GlobalElection)
admin.site.register(LocalElection)
admin.site.register(Candidate)
admin.site.register(Location)
admin.site.register(Voter)
