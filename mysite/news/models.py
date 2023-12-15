from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=75, default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Статья', max_length=2500, default='')
    date = models.DateTimeField('Дата публикации')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
