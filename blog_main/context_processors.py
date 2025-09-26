from aboutusfeatures.models import SocialLink
from blogs.models import Category
from blog_main import settings

def get_categories(request):
  categories = Category.objects.all().order_by('-created_at')
  return dict(categories=categories)

def get_social_links(request):
  social_links = SocialLink.objects.all()
  return dict(social_links=social_links)

def debug_mode(request):
  debug = settings.DEBUG
  return dict(debug=debug)