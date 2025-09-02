
---

### **2️⃣ retrieve.md**
```markdown
# Retrieve Book Details

```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()

# Retrieve first book details
b = Book.objects.first()
b.title, b.author, b.publication_year
