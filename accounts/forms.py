from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = User
    fields = ('email', )

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
      model = User
      fields = ('email', )