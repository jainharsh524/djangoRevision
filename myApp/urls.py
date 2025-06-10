from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('test/<str:id>/<str:name>', views.test, name = "test"),
    path('batch/<str:className>', views.batch, name = 'batch'),
    path('dept/<str:deptName>', views.department, name = 'department'),
    path('about/', views.about, name = "about")
]