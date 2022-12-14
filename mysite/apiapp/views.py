from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import Articleserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# @csrf_exempt
@api_view(['GET','POST'])
def article_list(request):
    if request.method=='GET':
        articles=Article.objects.all()
        serializer=Articleserializer(articles,many=True)
        # return JsonResponse(serializer.data,safe=False)
        return Response(serializer.data)

    elif request.method=='POST':
        # data=JSONParser().parse(request)
        # serializer=Articleserializer(data=data)
        serializer=Articleserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data,status=201)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(['GET','PUT','DELETE'])
def article_details(request,pk):
    try:
        article=Article.objects.get(pk=pk)
        print("article",article)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method=='GET':
        serializer=Articleserializer(article)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method=='PUT':
        # data=JSONParser().parse(request)
        # serializer=Articleserializer(article,data=data)
        serializer=Articleserializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors,status=400)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        article.delete()
        # return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)