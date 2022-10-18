from email.policy import default
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    inicio_fecha = models.DateTimeField(default = timezone.now)
    fin_fecha= models.DateTimeField(default = timezone.now)

    text = models.TextField(default = " ")
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) 
    lista_tags = (  ('Exp', 'Experiencia'),
                    ('Edu','Educacion'),
                    ('Hab','Habilidades'),
                    ('Pro','Projectos'),
                    ('Cer','Certificaciones')
                )
    tipo_post = models.CharField(max_length=3, choices=lista_tags ,default=('Exp', 'Experiencia'))   

    
   
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title