from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_staff",
        "is_active",
        "is_superuser",
        "last_login",
        "date_joined",
        "profile_pic",
        "address",
        "phone",
        "role",
        "bio",
    ]

    add_fieldsets = UserAdmin.add_fieldsets + (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "password1",
                "password2",
                "is_staff",
                "is_active",
                "is_superuser",
                "profile_pic",
                "address",
                "phone",
                "role",
                "bio",
            ),
        },
    )


admin.site.register(CustomUser, CustomUserAdmin)
