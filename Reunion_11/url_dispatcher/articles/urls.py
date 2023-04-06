from django.urls import path, re_path
from . import views

urlpatterns = [
    # Paths usando path
    # path('articles/2003/', views.special_case_2003),
    path('', views.index, name='articles-index'),
    path('articles/<int:year>/', views.year_archive, name='articles-year'),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    # Paths usando re_path
    path('articles/2003/', views.special_case_2003),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]
