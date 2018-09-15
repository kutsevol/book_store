from django.contrib import admin

from .models import Authors, Books, AuthorsToBooks


class AuthorsInline(admin.TabularInline):
    model = AuthorsToBooks
    extra = 0


@admin.register(Books)
class AdminBooks(admin.ModelAdmin):
    inlines = [AuthorsInline]


@admin.register(Authors)
class AdminAuthors(admin.ModelAdmin):
    pass
