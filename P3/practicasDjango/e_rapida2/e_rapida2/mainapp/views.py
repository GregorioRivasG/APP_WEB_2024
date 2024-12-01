from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests, 'mainapp/index.html',{
        'title':'Inicio | Página Principal',
        'content': 'Bienvenidos a la Pagina Principal'
    })

def about(requests):
    mensaje='Bienvenido'
    return render(requests, 'mainapp/about.html', {
        'tittle': 'Acerca de',
        'content':'Somos un grupo de Programadores',
        'mensaje': mensaje
    })


def mision(requests):
    return render(requests, 'mainapp/mision.html', {
        'tittle': 'Mision',
        'content':'Mision',
        
    })


def vision(requests):
    return render(requests, 'mainapp/vision.html', {
        'tittle': 'Nuestra Vision',
        'content':'Vision',
        
    })

def registro(requests):
    return render(requests, 'mainapp/registro.html', {
        'tittle': 'Registro',
        'content':'Registro',
        
    })

def iniciosesion(requests):
    return render(requests, 'mainapp/sesion.html', {
        'tittle': 'Login',
        'content':'Inicio Sesion',
        
    })