from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserProfileViewSet, BorrowRecordViewSet, BadgeViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserProfileViewSet)
router.register(r'borrow-records', BorrowRecordViewSet)
router.register(r'badges', BadgeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

