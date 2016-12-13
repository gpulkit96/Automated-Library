from django.contrib import admin
from catalogue.models import Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ('CallNum', 'Title', 'Author', )
admin.site.register(Post,PostAdmin)
# Register your models here.
