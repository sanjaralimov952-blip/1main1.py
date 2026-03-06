# 1main1.py
from django.db import models
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path
from django.shortcuts import get_object_or_404

# =======================
# MODELS
# =======================

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# =======================
# SERIALIZERS
# =======================

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


# =======================
# CATEGORY VIEWS
# =======================

@api_view(['GET'])
def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


# =======================
# PRODUCT VIEWS
# =======================

@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


# =======================
# REVIEW VIEWS
# =======================

@api_view(['GET'])
def reviews_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def review_detail(request, id):
    review = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


# =======================
# URLS
# =======================

urlpatterns = [
    path('api/v1/categories/', categories_list),
    path('api/v1/categories/<int:id>/', category_detail),

    path('api/v1/products/', products_list),
    path('api/v1/products/<int:id>/', product_detail),

    path('api/v1/reviews/', reviews_list),
    path('api/v1/reviews/<int:id>/', review_detail),
]
