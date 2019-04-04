from django import forms
from .models import Inward, InwardPic

class InwardForm(forms.ModelForm):
	class Meta:
		model = Inward
		fields = (
			'date_of_letter',
			'date_received',
			'received_from',
			'ref_no',
			'subject',
			'officer_to',
			'date_filed',
			'file_number'
			)
		labels = {'text':''}


class InwardPicForm(forms.ModelForm):
	class Meta:
		model = InwardPic
		fields = ('name', 'imagefile',)