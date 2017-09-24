from HTMLParser import HTMLParser
from urlparse import urlparse

class linkfinder(HTMLParser):
	"""docstring for linkfinder"""

	def __init__(self, base_URL, page_URL):
		
		self.base_URL = base_URL
		self.page_URL = page_URL
		self.links = set()

	def error(self, message):
				pass

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:
				if attribute == 'href':
					url = urlparse.urljoin(self.base_URL, value)
					self.links.add(url)

	def page_links(self):
		return self.links