# -*- coding: utf-8 -*-
# TODO: Write here your API ViewSets

from rest_framework.views import APIView
from rest_framework.response import Response
from .cynology_generator import CynologyGenerator
from .serializers import OwnerSerializer, DogSerializer, ChampionshipSerializer

class CynologyGeneratorViewSet(APIView):
    cynology_generator = CynologyGenerator(owners_number=10, dogs_number=20)

    def get(self, request, format=None):
        owners = self.cynology_generator.get_owners()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data)

    def get_dogs(self, request, format=None):
        dogs = self.cynology_generator.get_dogs()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def get_championships(self, request, format=None):
        championships = self.cynology_generator.get_championships()
        serializer = ChampionshipSerializer(championships, many=True)
        return Response(serializer.data)
