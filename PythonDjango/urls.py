from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<name>/', views.hello),
    path('schedule/', views.list_events),
    path('', RedirectView.as_view(url='/schedule/'))
]
