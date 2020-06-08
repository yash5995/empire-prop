from django.urls import path
from . import views
urlpatterns = [

path('', views.index, name='index'),
path('function/',views.index1,name='function'),
path('prediction/',views.prediction,name='prediction'),
path('calculate/',views.page,name='calculate'),
path('home/',views.home,name='home'),
path('contact/',views.contact,name='contact'),
path('about/',views.about,name='about'),
path('register/',views.register,name='register'),
path('login/',views.fetch,name='entry'),
path('Main/',views.checkUser,name='main'),
path('mail/',views.mail,name='mail'),
path('best_properties/',views.property,name='best'),
path('ganesh/',views.ganesh,name='ganesh'),
path('goyal/',views.goyal,name='goyal'),
path('keshar/',views.keshar,name='keshar'),
path('parshwa/',views.parshwa,name='parshwa'),
path('setu/',views.setu,name='setu'),
path('shree/',views.shree,name='shree'),
path('sobha/',views.sobha,name='sobha'),
path('saanvi/',views.saanvi,name='saanvi'),
]