from django.shortcuts import render
from django.views import generic
from catalogue.models import Post

class IndexView(generic.ListView):
	template_name="catalogue/catalogue.html"
	def get_queryset(self):
		return Post.objects.all().order_by("-date")[:25]
class DetailView(generic.DetailView):
	model=Post
	template_name="catalogue/post.html"

