from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication', 'auteur')
    search_fields = ('titre',)

admin.site.register(Article, ArticleAdmin)