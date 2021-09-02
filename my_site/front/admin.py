from django.contrib import admin
# Register your models here.
from .models import Book
from .models import Author
from .models import Publisher


admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
