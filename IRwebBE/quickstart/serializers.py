from rest_framework import serializers

# API for case matching
class TextProcessingSerializer(serializers.Serializer):
    input_text = serializers.CharField(max_length=10000)
    processed_text = serializers.CharField(read_only=True)



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