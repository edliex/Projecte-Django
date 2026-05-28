from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Autor, Tag
# Create your views here.

def starting_page(request):
    """
    Renderitza la pàgina principal amb els darrers tres posts publicats.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
    Returns:
        HttpResponse: La pàgina index.html amb el context dels posts recents.
    """
    posts = Post.objects.all().order_by("-data_publicacio")[:3]
    return render(request, "blog/index.html", {
        "posts": posts
    })

def posts(request):
    """
    Mostra un llistat complet de totes les publicacions del blog.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
    Returns:
        HttpResponse: La pàgina posts.html amb tots els objectes Posts.
    """
    posts = Post.objects.all()
    return render(request, "blog/posts.html", {
        "posts": posts
    })

def post_detail(request, slug):
    """
    Mostra el contingut detallat d'un post específic segons el seu slug.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
        slug (str): L'identificador únic del post que es vol visualitzar.
    Returns:
        HttpResponse: La pàgina post_detail.html amb les dades del post.

    """
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html",{
        "post": post
    })

def authors_list(request):
    """
    Mostra un llistat complet de tots els autors registrats al blog.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
    Returns:
        HttpResponse: La pàgina autors.html amb totes les dades de Autor.
    """
    autors = Autor.objects.all()
    return render(request, "blog/autors.html", {
        "autors": autors
    })

def author_detail(request, id):
    """
    Mostra els detalls d'un autor específic segons el seu identificador.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
        id (int): L'identificador únic de l'autor.
    Returns:
        HttpResponse: La pàgina autor_detail.html amb les dades de l'autor.
    """
    autor = get_object_or_404(Autor, id=id)
    return render(request, "blog/autor_detail.html",{
        "autor": autor
    })

def tag_list(request):
    """
    Mostra un llistat de totes les etiquetes (tags) utilitzades al blog.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
    Returns:
        HttpResponse: La pàgina tags.html amb tots els objectes Tag.
    """
    tags = Tag.objects.all()
    return render(request, 'blog/tags.html',{
        "tags": tags
    })

def tag_detail(request, id):
    """
    Mostra el detall d'una etiqueta específica segons el seu identificador.

    Args:
        request (HttpRequest): L'objecte de la petició de Django.
        id (int): L'identificador únic (clau primària) de l'etiqueta.
    Returns:
        HttpResponse: La pàgina tag_detail.html amb les dades de l'etiqueta.
    """
    tag = get_object_or_404(Tag, id=id)
    return render(request, "blog/tag_detail.html",{
        "tag": tag
    })
