from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = "home"),
    path('test/<str:id>/<str:name>', views.test, name = "test"),
    path('batch/<str:className>', views.batch, name = 'batch'),
    path('dept/<str:deptName>', views.department, name = 'department'),
    path('about/', views.about, name = "about"),
    path('users/', views.users, name="users")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
