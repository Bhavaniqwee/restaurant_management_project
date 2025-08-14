from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer
import requests
'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuAPIView(APIView):
    def get(self,request):
        menu=[
            {
            "name":"Margherita Pizza",
            "description":"Classic pizza with fresh mozzarella,tomatoes,and basil",
            "price":8.99
            },
            {
                "name":"Pasta Alfredo",
                "description":"Creamy sauce with fettuccine pasta",
                "price":10.50
            },
            {
                "name":"Caesar Salad",
                "description":"Fresh salad with Caesar dressing and croutons",
                "price":6.75
            }
        ]
        return Response(menu)

def menu_homepage(request):
    response=requests.get('http://127.0.0.1:8000/api/menu/')
    menu_data=response.json() if response.status_code==200 else []
    return render(request,'menu.html',{'menu':menu_data})