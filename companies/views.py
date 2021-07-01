from django.shortcuts import get_object_or_404, render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

# list all stocks n add new item to list
class StockList(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)

        return Response(serializer.data)

    def post(self):
        pass
