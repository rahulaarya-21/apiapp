from rest_framework import serializers
from apiapp.models import Article

# class Articleserializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     data = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title=validated_data.get('title',instance.title)
#         instance.author=validated_data.get('title',instance.author)
#         instance.email=validated_data.get('title',instance.email)
#         instance.date=validated_data.get('title',instance.data)
#         instance.save()
#         return instance

class Articleserializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        # fields=['id','title','author']
        fields='__all__'
