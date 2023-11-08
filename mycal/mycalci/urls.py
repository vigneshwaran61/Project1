from django.urls import path
from . import views


urlpatterns=[
    path('', views.index , name='index'),
    path('multi' , views.multi_inverse , name='multi'),
    path('about', views.about,name='about'),
    path('DSA',views.dsa_alg,name='dsa_al'),
    path('result',views.result,name='result'),
]