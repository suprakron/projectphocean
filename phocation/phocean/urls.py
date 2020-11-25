from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('Register/',views.Register, name="register"),
    path('karusart/',views.karusart, name="karusart"),
    path('logokmitl/',views.logokmitl, name="logokmitl"),
    path('prajom/',views.prajom, name="prajom"),
    path('pratep/',views.pratep, name="pratep"),
    path('satapat/',views.satapat, name="satapat"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('zone/',views.zone, name="zone"),
    path('engineer/',views.engineer, name="engineer")
    #login
    # path('image/',views.1.jpg,name="1.jpg")
]
