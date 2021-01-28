# from django.contrib import admin
# from django.urls import path
from django.urls import path
# from the_app.views import HomeView
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.HomeView, name = 'home'),
]
