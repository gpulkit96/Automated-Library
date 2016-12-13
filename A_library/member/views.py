from django.shortcuts import render
from django.views import generic
from member.models import Member

class IndexView(generic.ListView):
	template_name="member/member.html"
	def get_queryset(self):
		return Member.objects.all().order_by("-date")[:25]
class DetailView(generic.DetailView):
	model=Member
	template_name="member/Member.html"

