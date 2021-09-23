from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import PermissionsMixin

class UserAdmin(UserAdmin):
  add_form = UserCreationForm
  form = UserChangeForm
  list_display = ('is_staff', 'email', 'is_active',)
  list_filter = ('is_staff', 'email', 'is_active',)
  fieldsets = (
      (None, {'fields': ('email', 'password',)}),
      ('Permissions', {'fields': ('is_staff', 'is_active',)}),
  )

  add_fieldsets = (
      (None, {
          'classes':'wide',
          'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)
      })
  )
  search_fields = ('email',)
  ordering = ('email', )

# admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
