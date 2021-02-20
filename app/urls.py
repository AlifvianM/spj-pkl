from django.urls import path
from . import views


urlpatterns = [
    path('check-tanggal', views.check_tanggal),
    path('tambah-tanggal-merah', views.tanggal_merah_create, name='tambah-tanggal-merah'),
	path('<int:pk>/uraian', views.uraian, name='uraian'),
    path('tambah-spj', views.create_spj,name='tambah-spj'),
    path('', views.index, name='index')
]