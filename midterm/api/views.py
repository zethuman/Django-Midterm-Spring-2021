from django.shortcuts import render
from rest_framework import viewsets, renderers, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

# headers = ['Task', 'Created', 'Due on', 'Owner', 'Mark' ]
from api.models import Book, Journal
from api.serializers import BookSerializer, JournalSerializer, BookDetailSerializer, JournalDetailSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        elif self.action == 'books_detail':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return BookSerializer
        elif self.action == 'create':
            return BookSerializer
        elif self.action == 'update':
            return BookDetailSerializer
        elif self.action == 'destroy':
            return BookDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def books_detail(self, request, pk):
        queryset = Book.objects.filter(id=pk)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        elif self.action == 'journals_detail':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return JournalSerializer
        elif self.action == 'create':
            return JournalSerializer
        elif self.action == 'update':
            return JournalDetailSerializer
        elif self.action == 'destroy':
            return JournalDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def journals_detail(self, request, pk):
        queryset = Journal.objects.filter(id=pk)
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)


