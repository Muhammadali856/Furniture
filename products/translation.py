from modeltranslation.translator import register, TranslationOptions

from products import models


@register(models.ProductModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)