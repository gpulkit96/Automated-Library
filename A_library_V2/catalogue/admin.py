from django.contrib import admin
from catalogue.models import Post
from catalogue.models import Member

class PostAdmin(admin.ModelAdmin):
    search_fields = ('CallNum', 'Title', 'Author','Genre', )
class MemberAdmin(admin.ModelAdmin):
	search_fields = ('Name', 'RollNo')
admin.site.register(Member,MemberAdmin)
admin.site.register(Post,PostAdmin)
# Register your models here.
