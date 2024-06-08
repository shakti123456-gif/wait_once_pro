from django.contrib import admin

from mobileapi.models import User_mobile


class MyAdminSite(admin.AdminSite):
    site_header = "Monty Python administration"


admin_site = MyAdminSite(name="myadmin")
admin_site.register(User_mobile)
