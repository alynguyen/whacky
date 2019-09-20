from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('widget/create/', views.create_widget, name='create_widget'),
  path('widget/<int:pk>/rmv_widget/', views.WidgetDelete.as_view(), name='rmv_widget'),
]