from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),  
    # path('<int:uid>/',views.tgmap),      
    # path('<int:uid>/<str:lng>/',views.tgmap),      
    path('<int:uid>/lng<str:lng>lat<str:lat>/',views.tgmap),  
    path('products/<int:uid>/<str:sid>/<str:lat>/',views.tgmap),      
]
