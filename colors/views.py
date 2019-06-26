from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

from .models import ColorPalette, Image
from .serializers import ColorPaletteSerializer, ImageSerializer



def color_input(request):
    return render(request, 'build/index.html')


class ColorPaletteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows color palettes to be viewed or edited
    """
    permission_classes = (IsAuthenticated,)
    queryset = ColorPalette.objects.all()
    serializer_class = ColorPaletteSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else: 
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Images to be viewed or edited
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'uuid'

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else: 
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
        
