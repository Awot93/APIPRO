from django.contrib import admin
from .models import Link

# Register your models here.


class LinkAdmin(admin.LinkAdmin):
    list_display = ('target_url', 'description', 'identifier', 'author', 'created_date', 'active')

admin.site.register(Link, LinkAdmin)

