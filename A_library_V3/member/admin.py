from django.contrib import admin
from member.models import Member

class MemberAdmin(admin.ModelAdmin):
    search_fields = ('Name', 'Status', 'RollNo',)
    list_display = ('Name', 'RollNo','Dues','Status')
    list_filter = ('Name', 'RollNo','Dues','Status')
admin.site.register(Member,MemberAdmin)

# Register your models here.
