from django.conf.urls import url

from . import views
app_name='blog'
urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^article/(?P<article_id>[0-9]+)/$', views.view_article, name='view_article'),
	url(r'^genre/(?P<genre_id>[0-9]+)/$',views.view_genre, name='view_genre'),
]

