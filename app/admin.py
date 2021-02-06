from django.contrib import admin
from .models import Spj, Uraian
# Register your models here.

@admin.register(Spj)
class SpjAdmin(admin.ModelAdmin):
    list_display = ('nama_spj', 'pembuat')

@admin.register(Uraian)
class SpjAdmin(admin.ModelAdmin):
    list_display = ('surat_ke', 'spj_id')