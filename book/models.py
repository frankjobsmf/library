from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Nombre')
    last_name = models.CharField(max_length=30, verbose_name='Apellido')
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' ' + self.last_name

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
    status = models.BooleanField(verbose_name='Estado', default=False, null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.title