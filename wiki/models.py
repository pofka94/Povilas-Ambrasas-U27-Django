from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    image = models.FileField(null=True, blank=True, upload_to='images/%y/%m/%d/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        print(">>>",self.image, args, kwargs)
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)