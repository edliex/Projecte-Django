from django.db import models
from django.utils.text import slugify

# Create your models here.
class Posts(models.Model):
    """
    Representa una entrada del blog.

    Attributes:
        title (str): El títol del post.
        content (str): El contingut de l'article.
        image (ImageField): Imatge opcional associada a la publicació.
        published_date (datetime): Data de publicació generada automàticament.
        slug (str): Identificador amigable per a URLs, únic i indexat.
    """
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='posts_images', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=False, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        """
        Genera el slug automàticament a partir del títol abans de desar.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Autors(models.Model):
    """
    Representa un autor del blog amb la seva informació de contacte.

    Attributes:
        nom (str): Nom de l'autor.
        cognom (str): Cognom de l'autor.
        adreça (str): Correu electrònic de contacte.
        slug (str): Identificador generat a partir del nom complet.
    """
    nom = models.CharField(max_length=15)
    cognom = models.CharField(max_length=15)
    adreça = models.EmailField()
    slug = models.SlugField(blank=True, null=False, db_index=True, unique=True)


    def save(self, *args, **kwargs):
        """
        Genera el slug combinant nom i cognom abans de desar.
        """
        if not self.slug:
            self.slug = slugify(f"{self.nom} {self.cognom}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} {self.cognom}"

class Tag(models.Model):
    """
    Representa etiquetes per classificar les publicacions.

    Attributes:
        nom_tag (str): Nom de l'etiqueta.
        slug (str):  Identificador generat a partir del tag.
    """
    nom_tag = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, null=False, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        """
        Genera el slug a partir del nom de l'etiqueta.
        """
        if not self.slug:
            self.slug = slugify(self.nom_tag)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom_tag
    