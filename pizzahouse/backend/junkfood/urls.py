from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from junkfood import views

urlpatterns = [
    path('categories/', views.CategoriesList.as_view()),
    path('categories/<int:pk>/', views.CategoriesDetail.as_view()),
    path('menus/', views.MenusList.as_view()),
    path('menus/<int:pk>/', views.MenusDetail.as_view()),
    path('profiles/', views.ProfilesList.as_view()),
    path('profiles/<int:pk>/', views.ProfilesDetail.as_view()),
    path('supplements/', views.SupplementsList.as_view()),
    path('supplements/<int:pk>/', views.SupplementsDetail.as_view()),
]