# Update Book Title
```python
from bookshelf.models import Book
b = Book.objects.first()
b.title = "Nineteen Eighty-Four"
b.save()
b.title
```
**Expected Output:**
'Nineteen Eighty-Four'
