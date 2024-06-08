from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User_mobile,CustomerDetails,SubUser,Service,Therapist,Provider

# class UserAdmin(BaseUserAdmin):
#     list_display = ('email_address', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('email_address', 'first_name', 'last_name')
    

# admin.site.register(User_mobile)
# admin.site.register(CustomerDetails)
# admin.site.register(SubUser)
# admin.site.register(Service)
# admin.site.register(Therapist)
# admin.site.register(Provider)