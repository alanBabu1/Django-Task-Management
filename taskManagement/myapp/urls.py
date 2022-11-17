from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('main',views.mainPage,name='main'),
    path('create',views.create,name='create'),
    path('view',views.view,name='view'),
    path('assigned',views.assigned,name='assigned'),
    path('update/<str:pk>/',views.update,name='update'),
    path('delete/<str:pk>/',views.delete,name='delete'),
]