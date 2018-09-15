from django.db import models


class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Books(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Authors, blank=False,
                                     through='AuthorsToBooks')
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    @property
    def all_authors(self):
        return ', '.join(' '.join((author.last_name, author.first_name))
                         for author in self.authors.all())

    def __str__(self):
        return f"{self.all_authors} - {self.title}"

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class AuthorsToBooks(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)

    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'Author to book'
        verbose_name_plural = 'Authors to book'
