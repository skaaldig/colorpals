from rest_framework import serializers

from .models import ColorPalette, Image

from .helpers import get_colors, COLORPALETTE_FIELD_NAMES as CPFN

class ColorPaletteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ColorPalette
        fields = '__all__'


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        depth = 1
        fields = ('image', 'uuid', 'top_colors')

    def create(self, validated_data):
        colors = get_colors(validated_data['image'])
        colors = dict([(CPFN[count], rgb) for count, rgb in enumerate(colors)])
        colors = ColorPalette.objects.create(**colors)
        image = Image.objects.create(top_colors=colors, **validated_data)
        return image
