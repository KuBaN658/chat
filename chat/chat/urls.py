from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat_usb.urls')),
    path('', RedirectView.as_view(url='/chat/', permanent=True)),
    path('account/', include('account.urls'), name='account'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)