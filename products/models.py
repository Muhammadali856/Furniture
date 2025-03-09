from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class ProductCategoryModel(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('title'))
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT,
        null=True, blank=True,
        related_name='children',
        verbose_name=_('parent')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog category')
        verbose_name_plural = _('blog categories')


class ProductModel(BaseModel):
    image1 = models.ImageField(upload_to='blogs', verbose_name=_('image'))
    image2 = models.ImageField(upload_to='blogs', verbose_name=_('image'))
    title = models.CharField(max_length=128, verbose_name=_('title'))
    price = models.PositiveSmallIntegerField(verbose_name=_('integer'))


    categories = models.ManyToManyField(
        ProductCategoryModel,
        related_name='products',
        verbose_name=_('categories')
    )

    # tags = models.ManyToManyField(
    #     ProductTagModel,
    #     related_name='tags',
    #     verbose_name=_('tags')
    # )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')