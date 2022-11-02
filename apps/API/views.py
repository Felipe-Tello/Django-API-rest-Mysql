from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Pets
from .serializers import PetsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def pet_list(request):
    if request.method == 'GET':
        pets = Pets.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            pets = pets.filter(title__icontains=title)
        
        pets_serializer = PetsSerializer(pets, many=True)
        return JsonResponse(pets_serializer.data, safe=False)
 
    elif request.method == 'POST':
        pet_data = JSONParser().parse(request)
        pet_serializer = PetsSerializer(data=pet_data)
        if pet_serializer.is_valid():
            pet_serializer.save()
            return JsonResponse(pet_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Pets.objects.all().delete()
        return JsonResponse({'message': '{} Pets were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def pet_detail(request, pk):
    try: 
        pet = Pets.objects.get(pk=pk) 
    except Pets.DoesNotExist: 
        return JsonResponse({'message': 'The Pet does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        pet_serializer = PetsSerializer(pet) 
        return JsonResponse(pet_serializer.data) 
 
    elif request.method == 'PUT': 
        pet_data = JSONParser().parse(request) 
        pet_serializer = PetsSerializer(pet, data=pet_data) 
        if pet_serializer.is_valid(): 
            pet_serializer.save() 
            return JsonResponse(pet_serializer.data) 
        return JsonResponse(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        pet.delete() 
        return JsonResponse({'message': 'The Pet was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)