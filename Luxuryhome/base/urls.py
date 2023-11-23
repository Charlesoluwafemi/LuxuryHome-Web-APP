from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from searches.views import search_view

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about_page, name='about'),
    path('blog/<int:post_id>/', views.blog_post_detail_page, name='blog_post_detail'),
    path('blog/', views.blog_post_list_view, name='blog_post_list'), 
    path('blog/<int:post_id>/update/', views.blog_post_update_view, name='blog_post_update'),
    path('blog/<int:post_id>/delete/', views.blog_post_delete_view, name='blog_post_delete'),
    path('blog-new/', views.blog_post_create_view, name='blog_post_create'), 
    path('contact/', views.contact_page, name='contact_us'),
    path('search/', search_view, name='search'),  # Corrected the path and added the missing parenthesis
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
