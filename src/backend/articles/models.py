from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
