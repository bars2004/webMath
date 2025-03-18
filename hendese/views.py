from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from math import sqrt

class kvadratTenliyi(APIView):
    
    #permission_classes = [IsAuthenticated]
    
    class Meta:
        swagger_schema_fields = {
            'type': 'string',
            'title': 'File Content',
            'description': 'Content of the file base64 encoded',
            'read_only': False  # <-- FIX
        }
    
    @swagger_auto_schema(
        operation_description=" ax^2+bx+c=0 kvadrat tənliyini hesablamaq",
        manual_parameters=[
            openapi.Parameter(
                'a',  # Parameter name
                openapi.IN_QUERY,  # Location of the parameter (query string)
                description="a",  # Parameter description
                type=openapi.TYPE_NUMBER,  # Parameter type
                required=False  # Whether the parameter is required
            ),
            openapi.Parameter(
                'b',  # Parameter name
                openapi.IN_QUERY,  # Location of the parameter (query string)
                description="b",  # Parameter description
                type=openapi.TYPE_NUMBER,  # Parameter type
                required=False  # Whether the parameter is required
            ),
            openapi.Parameter(
                'c',  # Parameter name
                openapi.IN_QUERY,  # Location of the parameter (query string)
                description="c",  # Parameter description
                type=openapi.TYPE_NUMBER,  # Parameter type
                required=False  # Whether the parameter is required
            ),
        ],
        responses={200: openapi.Response('Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'message': openapi.Schema(type=openapi.TYPE_STRING)}))}
    )

    def get(self, request):
        a = float(request.GET.get('a', 0))        
        b = float(request.GET.get('b', 0))
        c = float(request.GET.get('c', 0))
        
        if(a==0):
            res = {"cavab": "a 0 ola bilməz"}
            return JsonResponse(res)

        d= b*b-4*a*c
        
        
        if(d>=0):
            x1=(-b+sqrt(d))/(2*a)
            x2=(-b-sqrt(d))/(2*a)
            res={"cavab":"2 fərqli kök var","x1":x1,"x2":x2}
        else:
            res={"cavab":"Kök yoxdur"}

        return JsonResponse(res)