from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
# Create your models here.
    
class Autor(models.Model):
    """
    Representa un autor del blog amb la seva informació de contacte.

    Attributes:
        nom (str): Nom de l'autor.
        cognom (str): Cognom de l'autor.
        adreça (str): Correu electrònic de contacte.
    """
    nom = models.CharField(max_length=15)
    cognom = models.CharField(max_length=15)
    adreça = models.EmailField()
    def nombre_posts(self):
        return self.posts.count()
    def __str__(self):
        return f"{self.nom} {self.cognom}"

class Tag(models.Model):
    """
    Representa etiquetes per classificar les publicacions.

    Attributes:
        nom_tag (str): Nom de l'etiqueta.
    """
    nom_tag = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_tag
    
class Post(models.Model):
    """
    Representa una entrada del blog.

    Attributes:
        titol (str): El títol del post.
        contingut (str): El contingut de l'article.
        imatge (ImageField): Imatge opcional associada a la publicació.
        data_publicacio (datetime): Data de publicació generada automàticament.
        autor (Autor): Clau forana a l'autor de la publicació. Pot ser nul.
        tags (Tag): Relació molts a molts amb les etiquetes de la publicació.
        slug (str): Identificador amigable per a URLs, únic i indexat.
    """
    titol = models.CharField(max_length=50, validators=[MinLengthValidator(5, message="El títol ha de tenir almenys 5 lletres.")])
    contingut = models.TextField()
    imatge = models.ImageField(upload_to='posts_images', null=True, blank=True)
    data_publicacio = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, related_name="posts")    
    tags = models.ManyToManyField(Tag, related_name="posts")
    slug = models.SlugField(blank=True, null=False, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        """
        Genera el slug automàticament a partir del títol abans de desar.
        """
        if not self.slug:
            self.slug = slugify(self.titol)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titol
