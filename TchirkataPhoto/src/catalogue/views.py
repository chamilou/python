from django.shortcuts import render, get_object_or_404
from catalogue.models import Product, Category
from django.http import request
from django.shortcuts import render_to_response
from time import timezone
from django.template.context import RequestContext

# Create your views here.


def index(request, template_name="catalog/index.html"):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    doc="HalloMyFriend it's me"
    return render_to_response(template_name, locals(), context_instance= RequestContext(request))
def show_category(request, category_slug, template_name="catalogue/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_product(request, product_slug):
    p = get_object_or_404(Product, slug = product_slug)
    pr =Product.objects.all()
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render_to_response('shoping_page.html', locals(),context_instance=RequestContext(request))
def shoping(request):
        #pr=get_object_or_404(Product)
        shoping_title ='Shoping_Page'
    
        pr =Product.objects.all()
        nombre_line = pr.count()
        #price = pr.order_by()
        
        catg= Category.objects.all()
       
        
        return render_to_response('shoping_page.html',locals()) 