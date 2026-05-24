from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Posts, Autors, Tag
# Create your views here.

def starting_page(request):
    """
    Renderitza la pàgina principal amb els darrers tres posts publicats.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
    Returns:
        HttpResponse: La pàgina index.html amb el context dels posts recents.
    """
    try:
        posts = Posts.objects.all().order_by("-published_date")[:3]
        return render(request, "blog/index.html", {
            "posts": posts
        })
    except:
        raise Http404()

def posts(request):
    """
    Mostra un llistat complet de totes les publicacions del blog.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
    Returns:
        HttpResponse: La pàgina posts.html amb tots els objectes Posts.
    """
    try:        
        posts = Posts.objects.all()
        return render(request, "blog/posts.html", {
            "posts": posts
        })
    except:
        raise Http404()

def post_detail(request, slug):
    """
    Mostra el contingut detallat d'un post específic segons el seu slug.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
        slug (str): L'identificador únic del post que es vol visualitzar.
    Returns:
        HttpResponse: La pàgina post_detail.html amb les dades del post.

    """
    post = get_object_or_404(Posts, slug=slug)
    return render(request, "blog/post_detail.html",{
        "post": post
    })