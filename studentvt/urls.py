
from django.contrib import admin
from django.urls import path
from timelec import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('convert/', views.transcribe_file_with_word_time_offsets, name="convert")
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
