from django import forms
from AppTwo.models import User

class new_user(forms.ModelForm):

    class Meta():
        model = User
        fields = '__all__'