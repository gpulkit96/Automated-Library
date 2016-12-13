from django.contrib import admin
from member.models import Member

class MemberAdmin(admin.ModelAdmin):
    search_fields = ('Name', 'RollNo')
admin.site.register(Member,MemberAdmin)

# Register your models here.
