from django.db import models
from django.contrib.auth.models import User


# One-to-Many: An Author can write many Books
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


# Many-to-One: A Book belongs to one Author
# Many-to-Many: A Book can be read by many Readers
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    readers = models.ManyToManyField(User, related_name="books_read")

    def __str__(self):
        return self.title


# One-to-One: A Profile is linked to exactly one User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

