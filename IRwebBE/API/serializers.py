from rest_framework import serializers

# API for case matching
class TextProcessingSerializer(serializers.Serializer):
    input_text = serializers.CharField(max_length=128)
    processed_text = serializers.CharField(read_only=True)

class ModelSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=65536)
    result = serializers.CharField(read_only=True)


'''
from django.contrib.auth.models import User, Group, Doc
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
'''