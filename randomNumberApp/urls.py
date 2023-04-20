from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index, name='index'),
    path('display_data/', views.display_data, name='display_data'),
]
