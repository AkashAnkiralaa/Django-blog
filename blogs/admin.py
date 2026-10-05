from django.contrib import admin

# Register your models here.
from .models import Category,Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # It auto genarte the slug in the page
    list_display = ('title','category','author','is_featured') 
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)