from django.urls import path
from autosapp.views import HomeModelosView, FichaModeloView, AutoRetrieveUpdateDestroyView, AutoListCreateView

urlpatterns = [
    path('autos/', HomeModelosView.as_view(), name='home_modelos'),
    path('autos/<int:pk>/', FichaModeloView.as_view(), name='ficha_modelo'),
    path('api/autos/', AutoListCreateView.as_view(), name='auto-list-create'),
    path('api/autos/<int:pk>/', AutoRetrieveUpdateDestroyView.as_view(), name='auto-retrieve-update-destroy')


]

