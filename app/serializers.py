from rest_framework import serializers 
from app.models import Persona, Intituto

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class IntitutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intituto
        fields = '__all__'
    