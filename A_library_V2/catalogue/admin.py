from django.contrib import admin
from catalogue.models import Post
#from .models import Post
class PostAdmin(admin.ModelAdmin):
    search_fields = ('CallNum', 'Title', 'Author','Genre', )
    list_display = ('CallNum', 'Title', 'Author','Genre', )
    list_filter = ('CallNum', 'Title', 'Author','Genre', )
admin.site.register(Post,PostAdmin)
# Register your models here.
