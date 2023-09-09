from django.shortcuts import render

# Create your views here.
# 'View' is Request Handler
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from IRwebBE.quickstart.serializers import TextProcessingSerializer

class ProcessTextView(APIView):
    def post(self, request, format=None):
        serializer = TextProcessingSerializer(data=request.data)

        if serializer.is_valid():
            input_text = serializer.validated_data['input_text']
            # 在这里编写处理文本的代码，例如对文本进行处理并赋值给 processed_text 变量
            processed_text = input_text.upper()  # 举例：将文本转换为大写

            return Response({'processed_text': processed_text}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from IRwebBE.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
'''