from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser,DoctorProfile,ShopManagerProfile,UserProfile,ContactUs


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ['usertype','profileupdated']}),
    )


admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)
admin.site.register(DoctorProfile)
admin.site.register(UserProfile)
admin.site.register(ShopManagerProfile)
admin.site.register(ContactUs)