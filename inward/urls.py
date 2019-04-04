from django.urls import path
from . import views

app_name = 'inward'
urlpatterns = [
	path('', views.index, name='index'),
	path('inward_list/', views.inward_list, name="inward_list"),
	path('inward_detail/<int:inward_id>/', views.inward_detail, name='inward_detail'),
	path('new_inward/', views.new_inward, name='new_inward'),
	path('edit_inward/<int:inward_id>/', views.edit_inward, name="edit_inward"),
	path('delete_inward/<int:inward_id>/', views.delete_inward, name="delete_inward"),
	path('list/', views.list, name='list'),
	path('upload/', views.upload, name='upload'),
	path('search/', views.search, name='search'),
]