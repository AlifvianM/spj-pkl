from django.shortcuts import render, redirect
from .forms import SpjForm, TanggalMerahForm
from .models import Spj, Uraian, TanggalMerah
from datetime import timedelta, date
from django.shortcuts import get_object_or_404

import datetime

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
    dt = datetime.datetime.now()
    dt_month = dt.month
    t_merah = TanggalMerah.objects.filter(tanggal_merah__month = dt_month)
    tanggal_list = [i.tanggal_merah.day for i in t_merah]
    if request.method == 'POST':
        form = SpjForm(request.POST)
        if form.is_valid():
            spj = form.save()
            print(spj.tgl_pembuatan.strftime("%A"))
            # if spj.tgl_pembuatan.day in tanggal_list:
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberian PPTK', tgl_pembuatan=date.today() + timedelta(days=4))
            #     return redirect('/')
            # else:
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberian PPTK', tgl_pembuatan=date.today() + timedelta(days=2))
            #     Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Permohonan Pengadaan',  tgl_pembuatan=date.today() + timedelta(days=4))
            #     return redirect('/')
            tgl_pemb = date.today() + timedelta(days=4)
            tgl_pemb2 = date.today() + timedelta(days=2)
            if (tgl_pemb.strftime("%A") == 'Saturday') or (tgl_pemb.strftime("%A") =='Sunday'):
                Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberian PPTK', tgl_pembuatan=tgl_pemb)
            else:
                Uraian.objects.create(spj_id=spj, surat_ke=Uraian.objects.filter(tgl_pembuatan__year=date.today().year).count() + 1, nama_uraian='Pemberian PPTK', tgl_pembuatan=tgl_pemb2)
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

def tanggal_merah_create(request):
    if request.method == 'POST':
        form = TanggalMerahForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = TanggalMerahForm()
    else:
        form = TanggalMerahForm()
    context = {
        'title':'Tambah Tanggal Merah',
        'form':form
    }
    return render(request, 'app/tanggal_merah_create.html', context)

def check_tanggal(request):
    dt = datetime.datetime.now()
    dt_month = dt.month
    print(dt_month)
    t_merah = TanggalMerah.objects.filter(tanggal_merah__month = dt_month)
    tanggal_list = [i.tanggal_merah.day for i in t_merah]
    # print(month_list)

    spj = Spj.objects.get(pk=24)
    spj_date = spj.tgl_pembuatan.day

    if spj_date in tanggal_list:
        print(True)
        Spj.objects.create(tgl_pembuatan= date.today() + timedelta(days=4))
    else:
        print(False)

    return render(request, 'app/check.html')