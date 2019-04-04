from efile.models import UserProfile
from django.core.files.images import get_image_dimensions
from allauth.account.forms import SignupForm
from django import forms

class SignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class PicForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('owner', 'picture',)
	
	# def clean_picture(self):
	# 	picture = self.cleaned_data['picture']

	# 	try:
	# 		w, h = get_image_dimensions(picture)
	# 		#validate dimensions
	# 		max_width = max_height = 100
	# 		if w > max_width or h > max_height:
	# 			raise forms.ValidationError(
	# 				u'Please use an image that is '
	# 				'%s x %s pixels or smaller.' % (max_width, max_height))

	# 		#validate content type
	# 		main, sub = picture.content_type.split('/')
	# 		if not (main == 'image' and sub in ['jpeg', 'jpg', 'gif', 'png']):
	# 			raise forms.ValidationError(u'Please use a JPEG, ' 'GIF or PNG image.')

	# 		#validate file size
	# 		if len(picture) > (20 *1024):
	# 			raise forms.ValidationError(
	# 				u'Picture file size may not exceed 20k.')

	# 	except AttributeError:
	# 		"""
	# 		Handle case when we are updating the user profile
	# 		and do not supply a new picture
	# 		"""
	# 		pass
	# 	return picture