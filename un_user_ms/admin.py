from django.contrib import admin

from un_user_ms.models import Profile
# Register your models here.
@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    pass
