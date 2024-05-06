from django.urls import path
import views

urlpatterns = [
    path('users/', views.create_user),
    path('users/all', views.get_all_users),
    path('users/user_id/', views.get_user),
    path('users/user_id/', views.update_user),
    path('users/user_id/', views.delete_user),
    path(url='https://ghibliapi.vercel.app')
]
