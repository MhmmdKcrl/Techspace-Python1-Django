from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, I

from recipes.models import Category, Tags, Recipe
from recipes.api.serializers import CategorySerializer, TagSerializer, RecipeSerializer, RecipeCreateSerializer

def categories(request):
    category_list = Category.objects.all()

    # data = []
    # for category in category_list:
    #     data.append(
    #         {
    #             'id': category.id,
    #             'name': category.name,
    #         }
    #     )
    # return JsonResponse(data, safe=False)

    serializer = CategorySerializer(category_list, many = True)
    return JsonResponse(serializer.data, safe=False)
    


def tags(request):
    tags_list = Tags.objects.all()
    serializer = TagSerializer(tags_list, many = True)
    return JsonResponse(serializer.data, safe=False)



@api_view(['GET', 'POST'])
def recipes(request):
    recipes_list = Recipe.objects.all()

    if request.method == "POST":
        serializer = RecipeCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status = 201)
        return JsonResponse(serializer.errors, safe=False, status = 403)
    
    serializer = RecipeSerializer(recipes_list, many = True,  context = {'request': request})
    return JsonResponse(serializer.data, safe=False, status = 200)


class RecipeListCreateApiView(ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    allowed_methods = ['GET', 'POST']

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = RecipeCreateSerializer
            
        return self.serializer_class


@api_view(['PUT', 'PATCH'])
def recipes_update(request, pk):

    recipe = Recipe.objects.get(id=pk)

    if request.method == "PUT":
        serializer = RecipeCreateSerializer(data = request.data, instance = recipe)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status = 201)
        return JsonResponse(serializer.errors, safe=False, status = 403)

    elif request.method == "PATCH":
        serializer = RecipeCreateSerializer(data = request.data, instance = recipe, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status = 201)
        return JsonResponse(serializer.errors, safe=False, status = 403)
    
    return JsonResponse(serializer.data, safe=False, status = 200)


class RecipeRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeCreateSerializer
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticated,]
