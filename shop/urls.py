from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.products_page, name='products'),
    url(r'^contacts$', views.contacts_page, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
