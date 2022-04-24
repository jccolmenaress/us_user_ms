
from un_user_ms.models import Profile
from un_user_ms.serializers import ProfileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


# Create your views here.
class ProfileCreate(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            print('request ',request.data['name'])
            serializer.save()
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    


class ProfileEdit(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404
    
    

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        fieldsModelProfile = ['email','name']
        fieldsRequest = list(request.data.keys())

        #reviso el campo email  va en la request
        email = fieldsModelProfile[0]
        if( email not in fieldsRequest):
            request.data[email] = profile.email
        
        #reviso el campo name  va en la request
        name= fieldsModelProfile[1]
        if( name not in fieldsRequest):
            request.data[name] = profile.name
        
        serializer = ProfileSerializer(profile, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk, format = None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        if(profile.status == True):
            return Response('usuario baneado', status= status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data )

    
        
    


class ProfileGet(APIView):
    
    def get(self, request, format = None):
        profile = Profile.objects.all().filter( name__icontains=request.data['name']).filter(status=False)
        serializer = ProfileSerializer(profile, many=True)
        if (serializer.data == []):
            return Response('No se encontro ningun resultado',status = status.HTTP_200_OK)
        return Response(serializer.data )
    


