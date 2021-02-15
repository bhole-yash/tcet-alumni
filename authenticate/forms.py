from django import forms
from django.contrib.auth.forms import UserCreationForm

from authenticate.models import Account

# Department =( 
#     ("COMP", "Computer Engineering"), 
#     ("ELEX", "Electronics Engineering"), 
#     ("MECH", "Mechanical Engineering"), 
#     ("CIVIL", "Civil Engineering"), 
#     ("EXTC", "Electronics & Telecommunication"), 
# ) 


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
	# Dept = forms.ChoiceField(choices = Department,required=True)

	class Meta:
		model = Account
		fields = ("email", "username", "password1",'department', "password2")
		





