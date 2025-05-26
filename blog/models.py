from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=600)
    description = RichTextUploadingField(
        config_name='special',
        external_plugin_resources=[(
            'youtube',
            'http://localhost:8000/static/ckeditor_plugins/youtube/youtube/',
            'plugin.js',
        )],
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            counter = 1
            original_slug = self.slug
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
