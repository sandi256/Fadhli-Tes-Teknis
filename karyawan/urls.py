from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.karyawan, name="karyawan"),
    path('update/<int:update_id>',views.update, name="karyawan_update")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
