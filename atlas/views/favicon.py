import os
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(60 * 60 * 24)
def icon(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    icon_path= os.path.join(base_dir,"static/atlas/images/favicon.ico")
    with open(icon_path,"rb") as f:
        return HttpResponse(f.read(),content_type="image/ico")
