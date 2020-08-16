from django.forms import ModelForm
from .models import Customer
class Customerform(ModelForm):
	class meta:
		model=Customer
		fields='__all__'