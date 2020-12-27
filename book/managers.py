#python
import datetime

from django.db import models

class BookManager(models.Manager):
    #Buscar libro por titulo
    def FindBookByTitle(self, title_param):
        return self.filter(
            title__icontains = title_param
        )

    #buscar libros por rango de fecha
    def FindBookByDateRange(self, date1, date2):
        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()

        return self.filter(
            published__range = (d1, d2)
        )

    #buscar libros por autor
    def FindBookByAuthor(self, author):
        return self.filter(
            author__name__icontains = author
        )