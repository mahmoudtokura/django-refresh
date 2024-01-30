from django.contrib import admin
from .models import Blog, Category, Comment


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
