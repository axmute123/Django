from rest_framework import serializers
from .models import database
class databaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = database
        fields = ['id','name','username']
