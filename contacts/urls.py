from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('delete/<int:pk>/', views.delete, name = 'delete'),
    path('create_contact', views.create, name='create'),
    path('edit/<int:pk>', views.edit_profile, name='edit'),
    path('profile/<int:pk>/', views.view_profile, name='profile'),
    path('', views.index, name='index'),
]