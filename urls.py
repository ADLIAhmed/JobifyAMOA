from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='jobify-home'),
    path('postanoffer/', views.postanoffer, name='jobify-postanoffer'),
    path('test/', views.test, name='jobify-test'),
    path('catagories/', views.categories, name='jobify-categories'),
    path('payment/', views.payment, name='jobify-payment'),
    path('responsepayment/', views.responsepayment, name='jobify-responsepayment'),
    path('offre/', views.offre, name='jobify-offre'),
    path('registration/', views.registration, name='jobify-registration'),
    path('profil/', views.profil, name='jobify-profil'),
    path('login/', views.login, name='jobify-login'),
    path('confirmation/', views.confirmation, name='jobify-confirmation'),
    path('confirmationhire/', views.confirmationhire, name='jobify-confirmationhire'),
    path('confirmationpayment/', views.confirmationpayment, name='jobify-confirmationpayment'),
    path('confirmationinteresse/', views.confirmationinteresse, name='jobify-confirmationinteresse'),
    path('interesse/', views.interesse, name='jobify-interesse'),
    path('offreetudiant/', views.offreetudiant, name='jobify-offreetudiant'),
    path('profils/', views.profils, name='jobify-profils'),
    path('offrepersonnalisee/', views.offrepersonnalisee, name='jobify-offrepersonnalisee'),
]