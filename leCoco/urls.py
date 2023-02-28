"""leCoco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Coque import views
from django import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('index/', views.hello),
    path('login/', views.login),
    path('reg/',views.reg),
    path('Terms/',views.Terms),
    path('AusF/',views.AusF),
    path('FranF/',views.FranF),
    path('ItaliaF/',views.ItaliaF),
    path('JaponF',views.JaponF),
    path('MexF/',views.MexF),
    path('SpainF/',views.SpainF),

    path('RecetaAP/',views.RecetaAP),
    path('RecetaBA/',views.RecetaBA),
    path('RecetaBB/',views.RecetaBB),
    path('RecetaCB/',views.RecetaCB),
    path('RecetaCO/',views.RecetaCO),
    path('RecetaCP/',views.RecetaCP),
    path('RecetaG/',views.RecetaG),
    path('RecetaMO/',views.RecetaMO),
    path('RecetaON/',views.RecetaON),
    path('RecetaPIM/',views.RecetaPIM),
    path('RecetaPOZ/',views.RecetaPOZ),
    path('RecetaPV/',views.RecetaPV),
    path('RecetaRAT/',views.RecetaRAT),
    path('RecetaRM/',views.RecetaRM),
    path('RecetaSC/',views.RecetaSC),
    path('RecetaSUS/',views.RecetaSUS),
    path('RecetaTE/',views.RecetaTE),
    path('RecetaTEMP/',views.RecetaTEMP),


]
