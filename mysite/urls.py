from django.contrib import admin
from django.urls import path, include
from polls import views  # 👈 Importamos home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls", namespace="polls")),  # <-- ¡CORRECTO!
    path('', views.home),  # 👈 Esta línea maneja la raíz "/"
]
