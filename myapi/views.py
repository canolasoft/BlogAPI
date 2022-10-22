from rest_framework import viewsets
import django_filters
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import(ListCreateAPIView)

# Consulta 0: dame los datos de la app
class DatappViewSet(viewsets.ModelViewSet):
	#queryset = Datapp.objects.all()
	serializer_class = DatappSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		return Datapp.objects.filter(keyapp = kap)

# index de prueba (muestra todos los canales)
def index(request):
	canales = Canal.objects.all().order_by('nombre_c')
	context = {'canales':canales}
	return render(request, "landing/index.html", context)

# Consulta 1: dame todos los Canales
class CanalesViewSet(viewsets.ModelViewSet):
	serializer_class = CanalSerializer
	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			return Canal.objects.all().order_by('nombre_c')

# Consulta 2: dame todas las Entradas de un Canal
class EntradasSerializer(ListCreateAPIView):
	serializer_class = EntradasSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_c = self.request.GET.get('id')
			entradas = Entrada.objects.filter(id_c__id_c = id_c)
			return entradas

# Consulta 2: dame todos los Wallpapers de un Artista
#class WallpaperSerializer(ListCreateAPIView):
#	serializer_class = WallpaperSerializer
#
#	def get_queryset(self):
#		kap = self.request.GET.get('kap')
#		if(Datapp.objects.filter(keyapp = kap)):
#			id_a = self.request.GET.get('id')
#			wallpapers = Wallpaper.objects.filter(id_a__id_a = id_a)
#			return wallpapers

# Consulta 3: dame los datos de un Canal
class CanalViewSet(viewsets.ModelViewSet):
	serializer_class = CanalSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_c = self.request.GET.get('id')
			return Canal.objects.filter(id_c = id_c)

# Consulta 4: dame las Redes de un Canal
class RedsocialSerializer(ListCreateAPIView):
	serializer_class = RedsocialSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_a = self.request.GET.get('id')
			redesociales = Redsocial.objects.filter(id_a__id_a = id_a)
			return redesociales

# Consulta 5: dame los datos de un Video
class EntradaSerializer(ListCreateAPIView):
	serializer_class = EntradaSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_e = self.request.GET.get('id')
			entrada = Entrada.objects.filter(id_e = id_e)
			return entrada