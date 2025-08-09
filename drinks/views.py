from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drinks_list(request):

    # get all the drinks from the database
    # serialize the data
    # return a JSON response

    drinks = Drink.objects.all()

    drink_serializer = DrinkSerializer(drinks, many=True)

    return JsonResponse({"drinks": drink_serializer.data}, safe=False)
