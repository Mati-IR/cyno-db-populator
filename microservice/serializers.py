# -*- coding: utf-8 -*-
from rest_framework import serializers

#TODO: write here your model serializers

from .models import Owner, Dog, Championship

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('owner_id',
                  'name',
                  'surname',
                  'breeding_nickname',
                  'membership_status',
                  'membership_type',
                  'phone_number',
                  'email',
                  'city',
                  'address',
                  'zip_code',
                  'dogs')

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('dog_id',
                  'race',
                  'sex',
                  'name',
                  'breeding_nickname',
                  'owner_id',
                  'date_of_birth',
                  'pedigree_number',
                  'branch_reg',
                  'color',
                  'litter',
                  'litter_card',
                  'medical_history')

class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = ('dog_id',
                  'championship_id',
                  'championship',
                  'date',
                  'judge')