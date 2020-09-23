from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('view_data/', views.view_data, name='view_data'),
    path('view_data/<str:data_id>/', views.detail_view, name='detail_view'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('update/<str:up_id>/', views.update_data, name='update'),
    path('delete_data/<str:del_id>/', views.delete_data, name='delete_data'),
]
