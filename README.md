# Django Article Project

## Overview
This is a Django-based web project that displays articles with a search feature. The website includes a homepage to view all articles and a navigation page to view individual articles. The project uses SQLite3 as the database.

## Features
- Displays recent articles on the homepage
- Search articles by heading
- Navigate to individual articles

## Technologies Used
- Django
- HTML/CSS
- SQLite3
- Bootstrap

## Usage
1. Run the project with `python manage.py runserver`
2. Access the admin panel to add articles
3. View the homepage to search and navigate through articles

## Snapshots
### Homepage
(day7/static/images/Screenshot 2025-01-09 130310.png)

### Navigation Page
(day7/static/images/Screenshot 2025-01-09 130349.png)

## Code Example
```python
from django.shortcuts import render
from .models import Article

def home(request):
    data1 = Article.objects.all()
    if request.method == "POST":
        search_query = request.POST.get('search')
        data1 = Article.objects.filter(h3__icontains=search_query)
    return render(request, 'index.html', {'data1': data1})
```

