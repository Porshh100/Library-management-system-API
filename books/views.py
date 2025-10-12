<<<<<<< HEAD
from django.shortcuts import render
=======
from rest_framework import viewsets
from .models import Book, UserProfile, BorrowRecord
from .serializers import BookSerializer, UserProfileSerializer, BorrowRecordSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer


>>>>>>> 17c612a (Added serializers, views, and URLs for API endpoints)

# Create your views here.
