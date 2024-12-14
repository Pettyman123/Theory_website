from django.urls import path
from . import views

urlpatterns = [
    path('', views.theory_list, name='theory_list'),
    path('<int:pk>/', views.theory_detail, name='theory_detail'),
    # path('<int:id>/', views.theory_detail, name='theory_detail'),
]



