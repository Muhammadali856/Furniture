from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



class BlogCategoryModel(models.Model):
    title = models.CharField(max_length=128, unique=True)
    parent = ForeignKey('self', on_delete=models.PROTECT, verbose_name=_('Parent'),
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
    title = models.CharField(max_length=128)
    image1 = models.ImageField(upload_to='blogs', null=True, blank=True)
    image2 = models.ImageField(upload_to='blogs', null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    long_description = models.TextField(max_length=2048, null=True, blank=True)
    
    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    tags = models.ManyToManyField(BlogTagModel, related_name='blogs')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        
class BlogCommentModel(models.Model):
    comment = models.CharField(max_length=128, verbose_name=_('Comment'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='blog_comments')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, verbose_name=_('Blog'), related_name='comments')


    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = _('Blog comment')
        verbose_name_plural = _('Blog comments')