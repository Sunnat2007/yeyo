from django.urls import path
from . import views
urlpatterns = [
    path('' , views.base , name='base'),
    path('uz/' , views.baseuz , name='baseuz'),
    path('en/' , views.baseen , name='baseen'),

    path('активность/' , views.aktivnost , name='aktivnost'),
    path('о_нас/' , views.onas , name='onas'),
    path('заказать/' , views.zakazat , name='zakazat'),
    path('регистр/' , views.registr , name='registr'),

    path('faoliyatimiz/' , views.faoliyat , name='faoliyat'),
    path('haqimizda/' , views.haqimizda , name='haqimizda'),
    path('buyurtma/' , views.buyurtma , name='buyurtma'),

]