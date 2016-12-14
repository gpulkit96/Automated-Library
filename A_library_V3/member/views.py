from django.shortcuts import render
from django.views import generic
from member.models import Member
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse

class IndexView(generic.ListView):
	template_name="member/member.html"
	def get_queryset(self):
		queryset_list =Member.objects.all().order_by("-date")
		query = self.request.GET.get("q")
		filter_q =  self.request.GET.get("f")
		if query:
			if filter_q=="Name":
				queryset_list = queryset_list.filter(Name__icontains =query)
			elif filter_q=="RollNo":
				queryset_list = queryset_list.filter(RollNo__icontains =query)
			elif filter_q=="Status":
				queryset_list = queryset_list.filter(Status__icontains =query)
		return queryset_list

class DetailView(generic.DetailView):
	model=Member
	template_name="member/post.html"
