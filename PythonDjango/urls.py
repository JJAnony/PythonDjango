from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<name>/', views.hello),
    path('login/', views.login_user),
    path('login/submit/', views.submit),
    path('logout/', views.logout_user),
    path('schedule/', views.list_events),
    path('', RedirectView.as_view(url='/schedule/'))
]
