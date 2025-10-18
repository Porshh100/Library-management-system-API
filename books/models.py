from django.db import models
from django.contrib.auth.models import User

# Represents each book in the library
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    copies_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


# Extends Django’s built-in User model with extra library info
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_membership = models.DateField(auto_now_add=True)
    active_status = models.BooleanField(default=True)
    total_books_borrowed = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username



# Tracks book borrowing and returning
class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    def save(self, *args, **kwargs):
        is_new = self._state.adding  # Check if it's a new record
        super().save(*args, **kwargs)

        if is_new:
            # Add points to the user's profile when borrowing
            profile = self.user.userprofile
            profile.points += 10  # 🎯 you can change 10 to any value
            profile.total_books_borrowed += 1
            profile.save()

            # Check if the user qualifies for new badges
            check_and_award_badges(profile)


# Badge model for user achievements
class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points_required = models.PositiveIntegerField()
    users = models.ManyToManyField(User, related_name='badges', blank=True)

    def __str__(self):
        return self.name


# Helper function to award badges
def check_and_award_badges(user_profile):
    badges = Badge.objects.filter(points_required__lte=user_profile.points)
    for badge in badges:
        if badge not in user_profile.user.badges.all():
            user_profile.user.badges.add(badge)

        
# Create your models here.
