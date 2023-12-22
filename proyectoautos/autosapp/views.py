from django.urls import reverse
from rest_framework import generics
from autosapp.models import Auto
from autosapp.serializers import AutoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.shortcuts import render
from django.db.models import Q


class HomeModelosView(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['modelo', 'tipo']

    def get(self, request, *args, **kwargs):
        tipos = Auto.TIPO_CHOICES
        autos = self.filter_queryset(self.get_queryset())

        # Extract selected tipo and order from query parameters
        selected_tipo = request.GET.get('tipo')
        selected_order = request.GET.get('orden')

        # Apply filters
        if selected_order == 'precio':
            autos = autos.order_by('precio')
        elif selected_order == '-precio':
            autos = autos.order_by('-precio')
        elif selected_order == 'anio':
            autos = autos.order_by('anio')
        elif selected_order == '-anio':
            autos = autos.order_by('-anio')

        # Apply additional filter if tipo is specified
        if selected_tipo:
            autos = autos.filter(tipo=selected_tipo)

            # Apply additional filter based on tipo
            if selected_order == 'newest':
                autos = autos.order_by('-anio')
            elif selected_order == 'oldest':
                autos = autos.order_by('anio')

        # Determine the active link based on the URL
        active_link = 'modelos' if request.path == reverse('home_modelos') else 'ficha'


        return render(request, 'autosapp/home_modelos.html', 
                      {'autos': autos, 
                       'tipos': tipos, 
                       'selected_tipo': selected_tipo,
                       'active_link': active_link,
                       'selected_order': selected_order
                       })



class FichaModeloView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

    def get(self, request, *args, **kwargs):
        auto = self.get_object()
        # Determine the active link based on the URL
        active_link = 'modelos' if request.path == reverse('home_modelos') else 'ficha'
        return render(request, 'autosapp/ficha_modelo.html', {'auto': auto,
                                                              'active_link': active_link,})




class AutoListCreateView(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class AutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
