from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'adminPanel/panel.html', context)
