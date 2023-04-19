"""bookHubBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from bookHubBackend import views
#from bookHubBackend.views import pdf_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



app_name = 'bookHubBackend'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('streamDetails/',views.streamDetails),
    path('', views.contactForm, name='contact'),
    path('product-details/',views.productDetails),
    path('engineering/',views.engineering),
    path('science/',views.science),
    path('commerce/',views.commerce),
    path('arts/',views.arts),  
    path('law/',views.law),
    path('medical/',views.medical),
    path('php/',views.php),
    path('python/',views.python),
    path('flutter/',views.flutter),
    path('react/',views.react),
    path('javascript/',views.javascript),
    path('bookDetails/',views.bookDetails),
    path('engineeringDetails/',views.engineeringDetails),
    path('semester1/',views.semester1),
    path('semester2/',views.semester2),
    path('semester3/',views.semester3),
    path('semester4/',views.semester4),
    path('semester5/',views.semester5),
    path('semester6/',views.semester6),
    path('semester7/',views.semester7),
    path('semester8/',views.semester8),
    path('main/', views.main, name='main'),
    re_path(r'^pdf', views.pdf, name='pdf'),
    path('view-pdf/', views.pdf_view,name='pdf_view'),
    path('view-pdf_display/', views.pdf_view,name='pdf_view_display'),
    # path('contact/',views.contact,name='contact'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)