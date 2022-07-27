from rest_framework import serializers
from fish.models import Data
from rest_framework.validators import UniqueValidator

class DataSerializer(serializers.ModelSerializer):

  upload = serializers.FileField(validators=[UniqueValidator(queryset=Data.objects.all())])

  class Meta:
    model = Data
    fields = ['upload']
    depth = 1


