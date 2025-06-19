from django import forms
from .models import Usuarios

class CreateDataForm(forms.ModelForm):
	class Meta:
		model = Usuarios
		#fields = ['nome', 'endereco', 'email', 'id']
		fields = '__all__'