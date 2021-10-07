from . models import Account
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
		class Meta:
			model = Account
			fields = ['id', 'username', 'email', 'department', 'first_name', 'last_name', 'password1', 'password2',]

# 	email		= forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'class':'form-control'}),help_text='Requried. Add a valid email address.')
# 	username 	= forms.CharField(label='Username', max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
# 	password1	= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
# 	password2	= forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
# 	class Meta:
# 		model 	= Account
# 		fields 	= ('username','email', 'password1', 'password2')
# 	def clean(self):
# 		username = self.cleaned_data['username']
# 		password1 = self.cleaned_data['password1']
# 		if len(password1) < 8:
# 			raise forms.ValidationError("password aleast 8 characters")
#
# class AccountAuthenticationForm(forms.ModelForm):
# 	username = forms.CharField(label='Username', max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
# 	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
# 	class Meta:
# 		model = Account
# 		fields = ('username', 'password')
#
# 	def clean(self):
# 		username = self.cleaned_data['username']
# 		password = self.cleaned_data['password']
# 		if not authenticate(username=username, password=password):
# 			raise forms.ValidationError("Incorrect username or password")
