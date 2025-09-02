# Delete Book

```python
from bookshelf.models import Book

# Delete the book
b = Book.objects.first()
b.delete()

# Confirm deletion
Book.objects.all()
```

**Expected Output:**
```
<QuerySet []>
```

