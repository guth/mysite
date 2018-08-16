from django.urls import path

from . import views

app_name = 'spojtools'
urlpatterns = [
	# /spojtools/
	path('', views.index, name='index'),
	path('compare/', views.compare, name='compare'),
]