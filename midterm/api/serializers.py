from rest_framework import serializers
from api.models import Book, Journal


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'


class JournalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
