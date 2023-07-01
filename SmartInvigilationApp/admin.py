from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'phone','date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'phone', 'username')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username','first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'profile_image', 'password1', 'password2'),
        }),
    )

    ordering=('email',)

class InvigilationStaffsAdmin(admin.ModelAdmin):
	list_display = ['username','camera_no','email','to_phone_number', 'created','updated']
	list_filter=['created','updated']


admin.site.register(MyUser, MyUserAdmin)	
admin.site.register(InvigilationStaffs,InvigilationStaffsAdmin)