from django.db import models

# Create your models here.

class Spj(models.Model):
    nama_spj                = models.CharField(max_length=255)
    pembuat                 = models.CharField(max_length=255)
    tgl_pembuatan           = models.DateField(auto_now_add=True)
    tgl_perubahan_terakhir  = models.DateField(auto_now=True, auto_now_add=False)
    
class Uraian(models.Model):
	nama_uraian 			= models.CharField(max_length=255, blank=True, null=True)
	surat_ke				= models.IntegerField(default=0)
	tgl_pembuatan 			= models.DateField(auto_now_add=True)
	tgl_perubahan_terakhir	= models.DateField(auto_now=True)
	spj_id					= models.ForeignKey(Spj, on_delete=models.CASCADE)

	def get_tgl_pembuatan_year(self):
		return self.tgl_pembuatan.year