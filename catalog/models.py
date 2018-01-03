from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.conf import settings


import uuid



image_storage = FileSystemStorage(
        location=u'{0}/'.format(settings.MEDIA_ROOT), 
        base_url=u'{0}/'.format(settings.MEDIA_URL),
        )

def image_directory_path(instance, filename):
    return u'{0}'.format(filename)

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre.")
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    photo = models.ImageField(upload_to="media/images/", null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    class Meta : 
        ordering = ["title"]
    
    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = 'Genre'
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    
    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)
        
    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)

    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    image = models.ImageField(upload_to="media/images/autheur", null=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    
    def get_books_count(self):
        return Book.objects.filter(author=self).count()
    
    def get_books_from_author(self):
        return Book.objects.filter(author=self)

    class Meta:
        ordering = ['last_name']
        
class Boutique(models.Model):
    name = models.CharField(max_length=100)
    open_year = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="media/images/boutiques", null=True, blank=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5)
    book = models.ManyToManyField('Book', blank=True) 
    
    def get_absolute_url(self):
        return reverse('boutique-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.id, self.name)

    class Meta:
        ordering = ['name']
        
@property
def is_overdue(self):
    if self.due_back and date.today() > self.due_back:
        return True
    return False

