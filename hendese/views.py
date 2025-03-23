from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .forms import kvadratTenliyiForm
from math import sqrt

class kvadratTenliyi(APIView):
    template_name = "kvadratTenliyi.html"
    form_class = kvadratTenliyiForm
    success_url = 'kvadrat/'
    parser_classes = (MultiPartParser,)
    
    #permission_classes = [IsAuthenticated]
    
    class Meta:
        swagger_schema_fields = {
            'type': 'string',
            'title': 'File Content',
            'description': 'Content of the file base64 encoded',
            'read_only': False  # <-- FIX
        }
    
    def get(self, request):
        res={"a":"a","b":"b","c":"c","form": kvadratTenliyiForm()}
        return render(request, self.template_name,res )
    
    @swagger_auto_schema(
        operation_description=" ax^2+bx+c=0 kvadrat tənliyini hesablamaq",
        manual_parameters=[
            openapi.Parameter(
                'a',  # Parameter name
                openapi.IN_FORM,  # Location of the parameter (query string)
                description="a",  # Parameter description
                type=openapi.TYPE_NUMBER,  # Parameter type
                required=False  # Whether the parameter is required
            ),
            openapi.Parameter( 'b', openapi.IN_FORM,  description="b", type=openapi.TYPE_NUMBER, required=False ),
            openapi.Parameter( 'c', openapi.IN_FORM,  description="c", type=openapi.TYPE_NUMBER, required=False ),
        ],
        responses={200: openapi.Response('Success', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'message': openapi.Schema(type=openapi.TYPE_STRING)}))}
    )
    
    def post(self, request):

        form = kvadratTenliyiForm(request.POST)

        res={"a":"a","b":"b","c":"c","form": kvadratTenliyiForm()}
        
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
        else:
            return render(request, self.template_name,res )

        if(a==0):
            res ["cavab"]= "a 0 ola bilməz"
            return render(request, self.template_name,res )#JsonResponse(res)

        d= b*b-4*a*c
        
        
        if(d>=0):
            x1=(-b+sqrt(d))/(2*a)
            x2=(-b-sqrt(d))/(2*a)
            res["cavab"]="2 fərqli kök var"
            res["x1"]=x1
            res["x2"]=x2
        else:
            res["cavab"]="Kök yoxdur"

        return render(request, self.template_name,res )#JsonResponse(res)
    



    