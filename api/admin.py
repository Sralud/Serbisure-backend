from django.contrib import admin
from .models import CustomUser, WorkerProfile, Service, Booking

admin.site.register(CustomUser)
admin.site.register(WorkerProfile)
admin.site.register(Service)
admin.site.register(Booking)
