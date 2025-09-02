
---

### **3️⃣ update.md**
```markdown
# Update Book Title

```python
from bookshelf.models import Book

# Update the title
b = Book.objects.first()
b.title = "Nineteen Eighty-Four"
b.save()

# Verify update
b.title
