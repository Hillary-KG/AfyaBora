from django import forms 
from .models import ClinicianLogin

class LoginForm(forms.ModelForm):
	class Meta:
		model = ClinicianLogin
		fields = ['email_address','password']
	#email validation 
	def clean_email_address(self):
		email = self.cleaned_data.get('email_address')
		emailBase,provider = email.split('@')
		domain,extension = provider.split('.')
		if not domain == 'health':
			raise forms.ValidationError("Please use a valid health staff email address")



	