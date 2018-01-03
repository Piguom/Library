from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Boutique
from import_export.admin import ImportExportModelAdmin

class BookAdmin(ImportExportModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    search_fields = ('title', 'author')
admin.site.register(Book, BookAdmin)

class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('last_name', 'first_name','date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    search_fields = ('first_name', 'last_name')
admin.site.register(Author, AuthorAdmin)

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {'fields': ('book','imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back','borrower')}),
    )

class GenreAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Genre, GenreAdmin)

@admin.register(Boutique)
class BoutiqueAdmin(ImportExportModelAdmin):
    list_display = ('name', 'open_year', 'street', 'city', 'zip_code')
