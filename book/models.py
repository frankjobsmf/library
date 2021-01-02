from django.db import models

#managers
from .managers import BookManager

#app reader / models
from reader.models import Reader

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre completo')
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')

    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre categoria')

    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Book(models.Model):
    title = models.CharField(max_length=20, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Autor')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoría')
    published = models.DateField(verbose_name='Publicado', null=True, blank=True)
    rented = models.BooleanField(verbose_name='Rentado', default=False, null=True, blank=True)

    #objects
    objects = BookManager()

    def __str__(self):
        return str(self.id) + ' - ' + self.title

class RentBook(models.Model):
    date_rent = models.DateField()
    date_return = models.DateField(blank=True, null=True)
    reader = models.ForeignKey(Reader, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    rented = models.BooleanField(default=False)
    
    def __str__(self):
        return self.reader.username + ' ' + str(self.date_rent)
    