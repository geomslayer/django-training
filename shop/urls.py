from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
