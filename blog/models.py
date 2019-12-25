from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags
from taggit.managers import TaggableManager
from PIL import Image
import markdown


class ArticleSection(models.Model):
    title = models.CharField(max_length=25, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    # modify_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    total_views = models.PositiveIntegerField(default=0)
    brief = models.TextField(blank=True)
    tags = TaggableManager(blank=True)
    avatar = models.ImageField(upload_to='article/%Y/%m%d/', default='article/default.jpg')
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

    def save(self, *args, **kwargs):
        article = super(Article, self).save(*args, **kwargs)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.brief = strip_tags(md.convert(self.content))[:10]
        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 256
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)
        return article
