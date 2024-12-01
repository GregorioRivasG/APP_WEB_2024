from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from articulos.models import Article,Category

# Create your views here.


@login_required(login_url='inicio')
def list_art(requests):

    #Sacar articulos de la BD
    articulos == Article.objects.all()


    return render(requests,'articulos/listado_art.html',{
        'title':'Articulos',
        'content':'Listado de Articulos',
        'articulos':articulos

    })

def list_cat(requests):

    categorias = Category.objects.all()
    return render(requests,'categorias/listado_cat.html',{
        'title':'Categorias',
        'content':'Listado de Categorias',

        'categorias':categorias
    })