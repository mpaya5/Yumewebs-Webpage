from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,
        verbose_name="Título")
    content = models.TextField(
        verbose_name="Contenido")
    published = models.DateTimeField(default=now,
        verbose_name="Fecha de publicación")
    image = models.ImageField(upload_to="blog", null=True, blank=True,
        verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True,
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,
        verbose_name="Fecha de edición")
    views = models.PositiveIntegerField(default = 0)

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ('title',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)