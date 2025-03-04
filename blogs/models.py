from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

class BlogCategoryModel(models.Model):
    title = models.CharField(max_length=128, unique=True)
    parent = ForeignKey('self', on_delete=models.PROTECT, 
                        null=True, blank=True, 
                        related_name='children')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class BlogTagModel(models.Model):
    title = models.CharField(max_length=128, unique=True)
    parent = ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class BlogModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')
        

