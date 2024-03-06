from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from FurnitureApp.serializers import FurnitureSerializer
from FurnitureApp.models import Product

@csrf_exempt
def furnitureApi(request,id=0):
    if request.method=='GET':
        product = Product.objects.all()
        product_serializer=FurnitureSerializer(product,many=True)
        return JsonResponse(product_serializer.data,safe=False)
    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        product_serializer=FurnitureSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
        product=Product.objects.get(id=id)
        product_serializer=FurnitureSerializer(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        product=Product.objects.get(id=id)
        product.delete()
        return JsonResponse("Deleted Successfully",safe=False)
