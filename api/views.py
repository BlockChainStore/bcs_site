from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
#from rest_framework.permissions import AllowAny
from django.http import HttpResponse, JsonResponse

# Create your views here.

class ownArea(APIView):
    def get(self, request, format='json'):
        return JsonResponse({"message":"SawaatDkub"})

    def post(self, request, format='json'):
        data = {
            'seller_address' : request.data.get('seller_address'),
            'latitude' : request.data.get('lat'),
            'longtitude' : request.data.get('lon'),
            'width' : request.data.get('width'),
            'length' : request.data.get('length'),
            'height' : request.data.get('height')
        }
        #seller_address = request.data.get('seller_address')
        #return HttpResponse(str(seller_address))
        #return JsonResponse(data)
        
        if data:
            return JsonResponse({"message": True, "Data": data})
        return JsonResponse({"message":"Input Wrong!!!"})

class regisProduct(APIView):
    def get(self, request, format='json'):
        return JsonResponse({"message":"SawaatDkub"})

    def post(self, request, format='json'):
        data = {
            'seller_address' : request.data.get('seller_address'),
            'p_hash' : request.data.get('p_hash')
        }
        if data:
            return JsonResponse({"message": True, "Data": data})
        return JsonResponse({"message":"Input Wrong!!!"})

class setPrice(APIView):
    def get(self, request, format='json'):
        return JsonResponse({"message":"SawaatDkub"})

    def post(self, request, format='json'):
        data = {
            'seller_address' : request.data.get('seller_address'),
            'p_hash' : request.data.get('p_hash'),
            'price' : request.data.get('price')
        }
        if data:
            return JsonResponse({"message": True, "Data": data})
        return JsonResponse({"message":"Input Wrong!!!"})

class activateProduct(APIView):
    def get(self, request, format='json'):
        return JsonResponse({"message":"SawaatDkub"})

    def post(self, request, format='json'):
        data = {
            'seller_address' : request.data.get('seller_address'),
            'p_hash' : request.data.get('p_hash')
        }
        if data:
            return JsonResponse({"message": True, "Data": data})
        return JsonResponse({"message":"Input Wrong!!!"})

class deactivateProduct(APIView):
    def get(self, request, format='json'):
        return JsonResponse({"message":"SawaatDkub"})

    def post(self, request, format='json'):
        data = {
            'seller_address' : request.data.get('seller_address'),
            'p_hash' : request.data.get('p_hash')
        }
        if data:
            return JsonResponse({"message": True, "Data": data})
        return JsonResponse({"message":"Input Wrong!!!"})

class buyProduct(APIView):
    def get(self, request, format='json'):
        return JsonResponse({"message":"SawaatDkub"})

    def post(self, request, format='json'):
        data = {
            'buyer_address' : request.data.get('buyer_address'),
            'p_hash' : request.data.get('p_hash')
        }
        if data:
            return JsonResponse({"message": True, "Data": data})
        return JsonResponse({"message":"Input Wrong!!!"})


"""
def ownArea(request, format='json'):
    data = {
        'seller_address' : request.data.get('seller_address'),
        'latitude' : request.data.get('lat'),
        'longtitude' : request.data.get('lon'),
        'width' : request.data.get('width'),
        'length' : request.data.get('length'),
        'height' : request.data.get('height')
    }
    if data:
        return JsonResponse({"message": "Input True"})
    return JsonResponse({"message":"Input Wrong!!!"})
    """
