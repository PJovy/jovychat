from django.db import models
from django.utils import timezone


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now())
    content = models.TextField()

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title
