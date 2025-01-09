
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

## Setup and Usage

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- SQLite3 (comes bundled with Python)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/django-article-project.git
   cd django-article-project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the website at `http://127.0.0.1:8000/`.

7. Visit the Django admin panel at `http://127.0.0.1:8000/admin/` to add or manage articles.

### Admin Panel Commands
- **Create Superuser**:  
  Run the following command to create an admin user:
  ```bash
  python manage.py createsuperuser
  ```

- **Access Admin Panel**:  
  Open your browser and go to `http://127.0.0.1:8000/admin/` to log in with the superuser credentials you created.

- **Run Server**:  
  Start the development server to run the project:
  ```bash
  python manage.py runserver
  ```

- **Apply Migrations**:  
  After modifying models, apply migrations to the database:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### Adding Articles via Admin Panel
1. After running the server, go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.
2. Under the "Articles" section, you can add new articles by specifying the title, content, author, and publication date.

### Running the Application
Once the server is running, open your browser and go to `http://127.0.0.1:8000/`. You'll see the homepage displaying all articles. You can search for articles by their heading or click on an article to view its details on a separate page.

## Snapshots
### Homepage
![Homepage](static/imgaes/home.png)

### Navigation Page
![Navigation Page](imgaes/navigation.png)

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
