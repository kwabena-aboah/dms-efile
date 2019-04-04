from django import forms
from .models import Outward, OutwardPic

class OutwardForm(forms.ModelForm):
	class Meta:
		model = Outward
		fields = (
			'date_received',
			'date_despatched',
			'subject',
			'ref_no',
			'address',
			'despatch_mode'
			)
		labels = {'text':''}


class OutwardPicForm(forms.ModelForm):
	class Meta:
		model = OutwardPic
		fields = ('name', 'imagefile',)