from django.contrib import admin
# Register your models here.
from .models import Book
from .models import Author
from .models import Publisher

# Add several columns to the admin site for Author
class AuthorAdmin(admin.ModelAdmin):
    list_display= ('first_name','last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    raw_id_fields = ('publisher',)
    ###
    # Which fields to be dsiplayed
    #fields = ('title',)
    ###
    filter_horizontal = ('authors',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Book,BookAdmin)
