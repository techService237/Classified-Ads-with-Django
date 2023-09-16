from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from index import views

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
    path('',include('index.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
