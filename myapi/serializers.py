# serializers.py
from rest_framework import serializers
from myapi.models import *

class CanalSerializer(serializers.HyperlinkedModelSerializer):
	id_tag = serializers.SlugRelatedField(read_only=True, slug_field='genero_tag')
	class Meta:
		model = Canal
		fields = ('id_c', 'nombre_c', 'imagen_c', 'descripcion_c', 'id_tag')

#class WallpaperSerializer(serializers.HyperlinkedModelSerializer):
#	id_a = serializers.SlugRelatedField(read_only=True, slug_field='nombre_a')
#	class Meta:
#		model = Wallpaper
#		fields = ('id_w', 'id_a', 'nombre_w', 'imagen_w')

class RedsocialSerializer(serializers.HyperlinkedModelSerializer):
	id_c = serializers.SlugRelatedField(read_only=True, slug_field='nombre_c')
	#id_rs = serializers.SlugRelatedField(read_only=True, slug_field='nombre_rs')
	class Meta:
		model = Redsocial
		fields = ('id_rs', 'id_c', 'nombre_rs', 'imagen_rs', 'url_rs')

class EntradasSerializer(serializers.HyperlinkedModelSerializer):
	id_c = serializers.SlugRelatedField(read_only=True, slug_field='nombre_c')
	id_tag = serializers.SlugRelatedField(read_only=True, slug_field='id_tag')
	#id_rs = serializers.SlugRelatedField(read_only=True, slug_field='nombre_rs')
	class Meta:
		model = Entrada
		fields = ('id_e', 'id_c', 'nombre_e', 'imagen_e', 'url_e', 'id_tag', 'texto_e')

class EntradaSerializer(serializers.HyperlinkedModelSerializer):
	id_c = serializers.SlugRelatedField(read_only=True, slug_field='nombre_c')
	id_tag = serializers.SlugRelatedField(read_only=True, slug_field='id_tag')
	class Meta:
		model = Entrada
		fields = ('id_e', 'id_c', 'nombre_e', 'imagen_e', 'url_e', 'id_tag')

#class RedsocialArtistaSerializer(serializers.ModelSerializer):
#	id_a = serializers.SlugRelatedField(read_only=True, slug_field='nombre_a')
#	id_rs = serializers.SlugRelatedField(read_only=True, slug_field='nombre_rs')
#	imagen_rs = serializers.SlugRelatedField(read_only=True, slug_field='imagen_rs')
	#redsocial = serializers.SlugRelatedField(read_only=True, slug_field='nombre_rs')
#
#	class Meta:
#		model = RedsocialArtista
#		fields = ('id_a', 'url_rsa', 'imagen_rs', 'id_rs')

class DatappSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Datapp
		fields = ('id', 'titulomapp', 'mensajeapp', 'linkapp', 'iconapp')