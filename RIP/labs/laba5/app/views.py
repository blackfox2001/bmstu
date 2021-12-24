from django.shortcuts import render
from app.models import Films


def GetFilms(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Список всех фильмов',
        'films': Films.objects.all()
    }})

def GetComedy(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Список комедий',
        'films': Films.objects.filter(idfilmgenre=2)
    }})

def GetMelodrama(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Список мелодрам',
        'films': Films.objects.filter(idfilmgenre=3)
    }})

def GetSciFi(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Список фантастики',
        'films': Films.objects.filter(idfilmgenre=1)
    }})

def GetFilm1(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Фильм 1',
        'films': Films.objects.filter(idfilm=1)
    }})

def GetFilm2(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Фильм 2',
        'films': Films.objects.filter(idfilm=2)
    }})

def GetFilm3(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Фильм 3',
        'films': Films.objects.filter(idfilm=3)
    }})

def GetFilm4(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Фильм 4',
        'films': Films.objects.filter(idfilm=4)
    }})

def GetFilm5(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Фильм 5',
        'films': Films.objects.filter(idfilm=5)
    }})

def GetFilm6(request):
    return render(request, 'home.html', {'data' : {
        'title': 'Фильм 6',
        'films': Films.objects.filter(idfilm=6)
    }})