from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('authentication.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('djoser.urls.authtoken')),
]
