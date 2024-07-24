# machine/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Beverage, Ingredient, BeverageIngredient
from .serializers import BeverageSerializer, IngredientSerializer

class BeverageListView(APIView):
    def get(self, request):
        # Retrieve all beverages from the database
        beverages = Beverage.objects.all()
        # Serialize the beverage data
        serializer = BeverageSerializer(beverages, many=True)
        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)

class DispenseBeverageView(APIView):
    def post(self, request):
        beverage_id = request.data.get('beverage_id')
        with_sugar = request.data.get('with_sugar', True)
        try:
            # Retrieve the beverage by ID
            beverage = Beverage.objects.get(id=beverage_id)
            ingredients = BeverageIngredient.objects.filter(beverage=beverage)

            # Check if sufficient ingredients are available
            for ingredient in ingredients:
                required_quantity = ingredient.quantity
                if ingredient.ingredient.name == 'Sugar' and not with_sugar:
                    required_quantity = 0
                if required_quantity > ingredient.ingredient.quantity:
                    return Response({'error': f'Insufficient {ingredient.ingredient.name} ingredients'}, status=status.HTTP_400_BAD_REQUEST)

            # Deduct the used ingredients from the inventory
            for ingredient in ingredients:
                used_quantity = ingredient.quantity
                if ingredient.ingredient.name == 'Sugar' and not with_sugar:
                    used_quantity = 0
                ingredient.ingredient.quantity -= used_quantity
                ingredient.ingredient.save()

            return Response({'message': f'{beverage} dispensed successfully'}, status=status.HTTP_200_OK)
        except Beverage.DoesNotExist:
            return Response({'error': 'Invalid beverage id'}, status=status.HTTP_400_BAD_REQUEST)

class InventoryListView(APIView):
    def get(self, request):
        # Retrieve all ingredients from the database
        ingredients = Ingredient.objects.all()
        # Serialize the ingredient data
        serializer = IngredientSerializer(ingredients, many=True)
        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)

class InventoryDetailView(APIView):
    def put(self, request, pk=None):
        try:
            # Retrieve the ingredient by ID
            ingredient = Ingredient.objects.get(id=pk)
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)

        # Partially update the ingredient data
        serializer = IngredientSerializer(ingredient, data=request.data, partial=True)
        if serializer.is_valid():
            # Check if the updated quantity exceeds the max capacity
            if 'quantity' in serializer.validated_data and serializer.validated_data['quantity'] > ingredient.max_capacity:
                return Response({'error': f'{ingredient.name} exceeds max capacity'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': 'Ingredient updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
