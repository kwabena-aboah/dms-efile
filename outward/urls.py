from django.urls import path
from . import views

app_name = 'outward'
urlpatterns = [
	path('outward_list/', views.outward_list, name="outward_list"),
	path('outward_detail/<int:outward_id>/', views.outward_detail, name='outward_detail'),
	path('new_outward/', views.new_outward, name='new_outward'),
	path('edit_outward/<int:outward_id>/', views.edit_outward, name="edit_outward"),
	path('delete_outward/<int:outward_id>/', views.delete_outward, name="delete_outward"),
	path('list/', views.list, name='list'),
	path('upload/', views.upload, name='upload'),
]