from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .strings import BLOG_STATUS
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_posts')
    post = RichTextUploadingField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=BLOG_STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Blog, self).save()
