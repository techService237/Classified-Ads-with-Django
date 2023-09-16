from django.http import HttpResponse
from django.shortcuts import render
from index.models import Ad 
from product.models import Product , Category

# Create your views here.

def indexpage(request):

	ads=Ad.objects.all()
	all_category = Category.objects.all()
	products = Product.objects.all()
	template = 'index.html'
	context = {'ads':ads, 'all_category' : all_category , 'products' : products}
	return render(request , template , context)


def form(request):
	return HttpResponse('A form')

def detailsAd(request):
	return HttpResponse('A details of a single app here')

