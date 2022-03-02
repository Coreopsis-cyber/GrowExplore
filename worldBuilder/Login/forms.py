from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Users
from crispy_forms.helper import FormHelper
# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	##Streaks = forms.CharField(required = False)
	class Meta:
		model = Users
		fields = ("username", "email", "password1", "password2", "Streaks")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.Streaks = ""
		if commit:
			user.save()
		return user

# class NewStreakForm(UserCreationForm):
#     Number = forms.IntegerField()
#     Location = forms.CharField(required = False)
#     class Meta:
#         model = Streak
#         fields = ("Location", "Number", "username")
#
#     def save(self, commit = True):
#         Streak = super(NewStreaksForm, self).save(commit=False)
#         if commit:
#             Streak.save()
#         return Streak

