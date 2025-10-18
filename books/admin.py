from django.contrib import admin
from .models import Book, UserProfile, BorrowRecord, Badge

# Register your models here.
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(BorrowRecord)
admin.site.register(Badge)
