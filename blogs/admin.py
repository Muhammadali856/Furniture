from django.contrib import admin
from .models import BlogModel, BlogCategoryModel, BlogTagModel, BlogCommentModel

admin.site.register(BlogModel)
admin.site.register(BlogCategoryModel)
admin.site.register(BlogTagModel)
admin.site.register(BlogCommentModel)
