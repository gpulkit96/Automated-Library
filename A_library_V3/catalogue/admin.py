from django.contrib import admin
from catalogue.models import Post
#from .models import Post
class PostAdmin(admin.ModelAdmin):
    search_fields = ('CallNum', 'Title', 'Author','Genre','Publisher' )
    list_display = ('CallNum', 'Title', 'Author','Genre', 'Publisher')
    #list_filter = ('Author','Genre','Publisher' )[:5]
admin.site.register(Post,PostAdmin)
# Register your models here.
