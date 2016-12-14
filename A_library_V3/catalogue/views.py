from django.shortcuts import render
from django.views import generic
from catalogue.models import Post
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse
from member.models import Member
class IndexView(generic.ListView):
	template_name="catalogue/catalogue.html"
	def get_queryset(self):
		queryset_list =Post.objects.all().order_by("-date")
		query = self.request.GET.get("q")
		filter_q =  self.request.GET.get("f")
		noviews = self.request.GET.get("i")
		if query:
			if filter_q=="Title":
				queryset_list = queryset_list.filter(Title__icontains =query)
			elif filter_q=="Author":
				queryset_list = queryset_list.filter(Author__icontains =query)
			elif filter_q=="Genre":
				queryset_list = queryset_list.filter(Genre__icontains =query)
			elif filter_q=="CallNum":
				queryset_list = queryset_list.filter(CallNum__icontains =query)
			elif filter_q=="Publisher":
				queryset_list = queryset_list.filter(Publisher__icontains =query)
		if noviews=="1-30":
			return queryset_list[:30]
		elif noviews=="1-50":
			return queryset_list[:50]
		elif noviews=="All":
			return queryset_list
		return queryset_list[:15]
class DetailView(generic.DetailView):
	model = Post
	template_name = "catalogue/post.html"
	'''
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		post_list = context['post']
		post_list.Status = Member.objects.get(id=(post_list.Status-1)).Name
		return context
	def save(self, *args, **kwargs):
		member= Member.objects.get(id=int('0' +self.model.Status))
		member.Status = self.model.Title
		member.save()
		super(Post, self).save(*args, **kwargs)'''