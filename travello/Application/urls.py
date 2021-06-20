from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.about, name='contact'),
    path('element.html', views.about, name='element'),
    path('news.html', views.about, name='news'),
    path('destinations.html', views.about, name='destination'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
