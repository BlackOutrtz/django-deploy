from django.db import models

class Personalidade(models.Model):
    class Meta:
        verbose_name = 'Personalidade'
        verbose_name_plural = 'Personalidades'

    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Atores(models.Model):
    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'

    primeiro_nome = models.CharField(max_length=50)
    segundo_nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=50)
    personalidade = models.ForeignKey(
        Personalidade,
        on_delete=models.SET_NULL,
        blank=True,
        null=True    
    )
    show = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    link_videos = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.primeiro_nome