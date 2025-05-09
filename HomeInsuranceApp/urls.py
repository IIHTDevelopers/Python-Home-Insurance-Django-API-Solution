"""HomeInsuranceApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from insuranceapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registeruser/',views.UserRegisterView.as_view()),
    path('createquote/',views.QuoteView.as_view()),
    path('getquote/',views.QuoteView.as_view()),
    path('buypolicy/',views.BuyPolicyView.as_view()),
    path('showpolicy/<int:pk>/',views.ShowPolicyView.as_view()),
    path('renewpolicy/<int:pk>/',views.RenewPolicyView.as_view()),
    path('cancelpolicy/<int:pk>/',views.CancelPolicyView.as_view()),
]
