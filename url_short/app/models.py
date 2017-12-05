from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from hashids import Hashids
hashids = Hashids()

class Link(models.Model):
	url = models.URLField()

	def get_absolute_url(self):
		return reverse("link_show", kwargs={"pk": self.pk})


	@staticmethod
	def shorten(link):
		l, _ = Link.objects.get_or_create(url=link.url)
		return str(hashids.encrypt(l.pk))

	@staticmethod
	def show(slug):
		dirty_str = str(hashids.decrypt(slug))
		clean_id = dirty_str.strip("(,)")
		link_id = int(clean_id)
		l = Link.objects.get(pk=link_id)
		return l.url

	def short_url(self):
		return reverse("redirect_short_url",
                   kwargs={"short_url": Link.shorten(self)})
