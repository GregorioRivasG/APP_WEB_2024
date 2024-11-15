from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests, 'mainapp/index.html',{
        'title':'Inicio | Página Principal',
        'content': 'Bienvenidos a la Pagina Principal'
    })

def about(requests):
    mensaje='Somos un equipo destinado al desarrollo de SW'
    return render(requests, 'mainapp/about.html', {
        'tittle': 'Acerca de Nosotros',
        'content':'Acerca de Nosotros',
        'mensaje': mensaje
    })


def mision(requests):
    return render(requests, 'mainapp/mision.html', {
        'tittle': 'Mision de la Empresa',
        'content':'Mision',
        
    })


def vision(requests):
    return render(requests, 'mainapp/vision.html', {
        'tittle': 'Nuestra Vision',
        'content':'Vision',
        
    })

def redirigir_inicio(request,exception):
    return render(request,'mainapp/404.html')