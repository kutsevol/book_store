import logging

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


LOG_LEVELS = (
    (logging.NOTSET, _('NotSet')),
    (logging.INFO, _('Info')),
    (logging.WARNING, _('Warning')),
    (logging.DEBUG, _('Debug')),
    (logging.ERROR, _('Error')),
    (logging.FATAL, _('Fatal')),
)


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
    published_date = models.DateField(default=timezone.now)

    @property
    def all_authors(self):
        return ', '.join(' '.join((author.last_name, author.first_name))
                         for author in self.authors.all())

    @staticmethod
    def get_absolute_url():
        return reverse('books')

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


class StatusLog(models.Model):
    logger_name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(
        choices=LOG_LEVELS, default=logging.ERROR, db_index=True)
    msg = models.TextField()
    trace = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.msg

    class Meta:
        ordering = ('-create_datetime',)
