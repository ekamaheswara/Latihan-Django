from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul': 'About',
        'judul2': 'About',
        'paragraf': 'Website ini dibuat menggunakan django',
        'nav': [
            ['/', 'Home'],
        ]
    }
    return render(request,'about.html', context)