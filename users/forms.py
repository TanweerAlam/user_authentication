from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('first_name', 'last_name', 'email', 'username', 'date_of_birth')
		# fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'date_of_birth')
		widgets = {
			'date_of_birth' : forms.DateInput(format=('%m%d%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
		}


		
class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('first_name', 'last_name', 'username', 'date_of_birth')
		# fields = UserChangeForm.Meta.fields