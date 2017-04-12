from django.http import HttpResponse,Http404
from django.shortcuts import render

from .models import Article,Genre 
def index(request):
    return render(request,'blog/index.html',{'genres':Genre.objects.all(),'articles':Article.objects.all()[:3]})

def view_article(request, article_id):
	try:
		a=Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article Doesn't Exist!")
	return render(request,'blog/view_article.html',{'article':a})

def view_genre(request, genre_id):
	try:
		g=Genre.objects.get(pk=genre_id)
	except Genre.DoesNotExist:
		raise Http404("Genre Doesn't Exist!")
	return render(request,'blog/view_genre.html',{'genre':g,'articles':Article.objects.filter(genre=g)[:5]})
