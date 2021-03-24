from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    context = {
        'judul':'Selamat Datang',
        'judul2':'di website kami',
        'paragraf':'Website ini dibuat menggunakan django',
        'nav':[
            ['/blog','Blog'],
            ['/about','About'],
        ]
    }


    return render(request,'index.html', context)

# def about(request):
#     return HttpResponse("<h2>Tentang</h2>")