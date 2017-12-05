from django.shortcuts import render

from django.views.generic import CreateView,DetailView,RedirectView
from .models import Link
from django.shortcuts import redirect


class LinkCreate(CreateView):
	model = Link
	fields = ["url"]

	def form_valid(self, form):
		prev = Link.objects.filter(url=form.instance.url)
		if prev:
			return redirect("link_show", pk=prev[0].pk)
		return super(LinkCreate, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(LinkCreate, self).get_context_data(**kwargs)
		context['link_list'] = Link.objects.all().order_by('-id')[:10]
		context['site_url'] = "r.a"
		return context

class LinkShow(DetailView):
	model = Link
	def get_context_data(self, **kwargs):
		context = super(LinkShow, self).get_context_data(**kwargs)
		context['site_url'] = "r.a"
		return context


class ShowURL(RedirectView):
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		short_url = kwargs["short_url"]
		return Link.show(short_url)
