# Delete Book
```python
from bookshelf.models import Book
b = Book.objects.first()
b.delete()
Book.objects.all()
```
**Expected Output:**
<QuerySet []> 
