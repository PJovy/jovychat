from django.db import models
from django.utils import timezone


class ArticleSection(models.Model):
    title = models.CharField(max_length=25, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    total_views = models.PositiveIntegerField(default=0)
    section = models.ForeignKey(
        ArticleSection,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return self.title
