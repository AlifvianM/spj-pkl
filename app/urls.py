from django.urls import path
from . import views


urlpatterns = [
	path('<int:pk>/uraian', views.uraian, name='uraian'),
    path('tambah-spj', views.create_spj,name='tambah-spj'),
    path('', views.index, name='index')
]