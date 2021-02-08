from django.shortcuts import render, redirect
from .forms import SpjForm
from .models import Spj, Uraian
from datetime import timedelta, date
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    title = 'List SPJ'
    spj = Spj.objects.all().order_by('-tgl_pembuatan')
    context = {
        'title':title,
        'spjs':spj
    }
    return render(request, 'app/index.html', context)

def create_spj(request):
    title = 'Tambah SPJ'
    if request.method == 'POST':
        form = SpjForm(request.POST)
        if form.is_valid():
            spj = form.save()
            # print(Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count())
            Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberian PPTK', tgl_pembuatan=date.today() + timedelta(days=2))
            Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pengadaan',  tgl_pembuatan=date.today() + timedelta(days=4))
            return redirect('/')
        else:
            pass
    else:
        form = SpjForm()
    context = {
        'title' : title,
        'form' : form
    }
    return render(request, 'app/form_spj.html', context)

def uraian(request, pk):
    # obj = get_object_or_404(Uraian, pk=pk)
    objs = Uraian.objects.filter(spj_id=pk)
    # title = '{} - {}'.format(obj.nama_uraian, obj.id)
    context = {
        'objs':objs,
        'title':'Uraian'
    }
    return render(request, 'app/uraian.html', context)








