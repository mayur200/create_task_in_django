from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import TaskSerializer
# from .models import Task

class TaskView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    # parser_classes = (MultiPartParser,)
    def post(self, request, *args, **kwargs):
        file_serializer = TaskSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        # do some stuff with uploaded file
        file_serializer = TaskSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(status=204)





 