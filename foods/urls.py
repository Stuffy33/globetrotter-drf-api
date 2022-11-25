from django.urls import path
from foods import views

urlpatterns = [
    path('foods/', views.FoodList.as_view()),
    path('foods/<int:pk>/', views.FoodDetail.as_view())
]