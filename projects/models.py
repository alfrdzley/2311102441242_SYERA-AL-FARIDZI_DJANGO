from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=600)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    client = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    services = models.CharField(max_length=200)
    project_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            counter = 1
            original_slug = self.slug
            while Project.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
