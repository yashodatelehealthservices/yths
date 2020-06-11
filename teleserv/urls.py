from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	 path('TeleEducation',views.TeleEducation,name='TeleEducation'),
	 path('Diet',views.TeleDietics,name='TeleDietics'),
	 path('index',views.index,name='index'),
	 path('Pathology',views.Pathology,name='Pathology'),
	 path('Online',views.Online,name='Online'),
]
	