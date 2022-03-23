from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=200,
        verbose_name="Título")
    subtitle = models.CharField(max_length=400,
        verbose_name="Subtítulo")
    image = models.ImageField(upload_to="portfolio", null=True, blank=True,
        verbose_name="Imagen")
    fecha = models.CharField(max_length=50, null=True,
        verbose_name="Fecha de creación")
    concept = models.TextField(null=True,
        verbose_name="Concepto del Proyecto")
    mockup = models.ImageField(upload_to="portfolio", null=True, blank=True,
        verbose_name="Mockup")
    development = models.TextField(null=True,
        verbose_name="Desarrollo del proyecto")
    page1 = models.ImageField(upload_to="portfolio", null=True, blank=True,
        verbose_name="Primera imagen de la web")
    page2 = models.ImageField(upload_to="portfolio", null=True, blank=True,
        verbose_name="Segunda imagen de la web")
    url = models.URLField(max_length=200, null=True,
        verbose_name="Url del sitio web")
    created = models.DateTimeField(auto_now_add=True,
        verbose_name="Fecha")
    updated = models.DateTimeField(auto_now=True,
        verbose_name="Fecha de actualización")
    odd = models.BooleanField(null=True, blank=True,
        verbose_name="Impar")
    even = models.BooleanField(null=True, blank=True,
        verbose_name="Par")
    
    class Meta:
        verbose_name = "trabajo"
        verbose_name_plural = "trabajos"
        ordering = ('id',)

    def __str__(self):
        return self.title

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if not url.startswith('http://'):
            url = 'http://' + url
        return url