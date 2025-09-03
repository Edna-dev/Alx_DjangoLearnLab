# Retrieve Book Details

```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()

# Retrieve first book details
b = Book.objects.first()
b.title, b.author, b.publication_year
```

**Expected Output:**
```
<QuerySet [<Book: Book object (1)>]>
('1984', 'George Orwell', 1949)
```
