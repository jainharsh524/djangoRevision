---

## 🌳 Chapter 5: Template Inheritance & Static Files

In this chapter, we’ll learn how to **reuse templates** via inheritance and how to serve **static assets** (CSS, JavaScript, images) in Django. This is essential for building consistent layouts and styling your pages.

---

### 1. Template Inheritance

#### 🔍 Why Use Template Inheritance?

* Avoid duplication of common HTML (e.g., `<head>`, navigation bar, footer).
* Maintain a single “base” layout, and let individual pages fill in specific content.
* Makes it easier to update shared sections across the site.

#### 🛠️ Steps to Implement Template Inheritance

1. **Create a `base.html`** in a templates directory.
2. **Define “blocks”** in `base.html` that child templates can override.
3. **Extend `base.html`** in your page-specific templates and provide content for those blocks.

#### 📁 Directory Structure Example

```
myFirstProjectInDjango/
├── myapp/
│   ├── templates/
│   │   ├── base.html
│   │   └── home.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── myFirstProjectInDjango/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

> Note: You can also organize templates per app, e.g., `myapp/templates/myapp/base.html` and configure `TEMPLATES` setting appropriately. For simplicity, here we assume Django will find `templates/` in each app.

---

#### 🔹 Example `base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Django Site{% endblock %}</title>
    {% load static %}
    <!-- Example: link to a CSS file -->
    <link rel="stylesheet" href="{% static 'myapp/css/styles.css' %}">
    {% block extra_head %}
    <!-- Child pages can add extra <head> elements here -->
    {% endblock %}
</head>
<body>
    <!-- Example header / navbar -->
    <header>
      <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'about' %}">About</a>
        <!-- Add more navigation links -->
      </nav>
    </header>

    <main>
      {% block content %}
      <!-- Default content; overridden by child templates -->
      {% endblock %}
    </main>

    <footer>
      <p>&copy; 2025 My Django Site</p>
    </footer>

    <!-- Example: include a JS file -->
    <script src="{% static 'myapp/js/main.js' %}"></script>
    {% block extra_scripts %}
    <!-- Child pages can add extra scripts here -->
    {% endblock %}
</body>
</html>
```

* `{% block title %}`: child templates override this to set page title.
* `{% block extra_head %}`: optional extra head tags (e.g., meta tags, additional CSS).
* `{% block content %}`: main body content.
* `{% block extra_scripts %}`: place for page-specific JavaScript.
* `{% load static %}`: required at top of template when using `{% static %}` tag.

#### 🔹 Example Child Template: `home.html`

```html
{% extends 'base.html' %}

{% block title %}Home - My Django Site{% endblock %}

{% block content %}
  <h1>Welcome to the Home Page</h1>
  <p>This is the homepage content.</p>
{% endblock %}
```

* We use `{% extends 'base.html' %}` to inherit.
* Override blocks as needed.

#### 🔹 Another Child Template: `about.html`

```html
{% extends 'base.html' %}

{% block title %}About Us{% endblock %}

{% block content %}
  <h1>About Us</h1>
  <p>Information about the site or author.</p>
{% endblock %}
```

#### 🔹 views and urls

In `views.py`:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
```

In `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

---

### 2. Static Files

#### 🔍 What Are Static Files?

* Files like CSS, JavaScript, images, fonts—assets that don’t change per request.
* During development, Django can serve them; in production, typically served by a web server (e.g., Nginx).

#### 🛠️ Configure Static Files in `settings.py`

Ensure in your `settings.py` you have:

```python
import os
# ...

# URL to use when referring to static files located in STATICFILES_DIRS.
STATIC_URL = '/static/'

# During development, Django automatically looks into 'static/' directories of each app.
# If you want to define additional directories for static files:
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # e.g., project-level static folder
]
# For production collectstatic target directory:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # used when running collectstatic
```

* `BASE_DIR` is usually defined at top of settings.
* `STATIC_URL` is the prefix used in templates: `{% static 'path/to/file' %}` will resolve to `/static/path/to/file`.
* During development (`DEBUG=True`), `runserver` automatically serves static files from app-level `static/` folders and any paths in `STATICFILES_DIRS`.
* In production, you run `python manage.py collectstatic` to gather all static files into `STATIC_ROOT`, then configure your web server to serve `/static/` from there.

#### 📁 Organizing Static Files

1. **App-level static**: Inside each app, create a `static/` folder:

   ```
   myapp/
   ├── static/
   │   └── myapp/
   │       ├── css/
   │       │   └── styles.css
   │       ├── js/
   │       │   └── main.js
   │       └── images/
   │           └── logo.png
   ```

   * Note: nesting under `myapp/` namespace avoids name collisions.
   * To reference `styles.css`, use `{% static 'myapp/css/styles.css' %}`.

2. **Project-level static** (optional):

   ```
   project_root/
   ├── static/
   │   ├── global.css
   │   └── images/
   │       └── banner.jpg
   ```

   * Add this folder in `STATICFILES_DIRS`.
   * Can be useful for assets shared across multiple apps.

#### 🔹 Example CSS File: `styles.css`

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header nav {
    background-color: #333;
    color: #fff;
    padding: 1rem;
}

header nav a {
    color: #fff;
    margin-right: 1rem;
    text-decoration: none;
}

main {
    padding: 2rem;
}
```

#### 🔹 Example JavaScript File: `main.js`

```javascript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Page loaded');
    // Add interactive behaviors here
});
```

#### 🔹 Using Static Files in Templates

In `base.html` (as shown earlier):

```html
{% load static %}
<link rel="stylesheet" href="{% static 'myapp/css/styles.css' %}">
...
<script src="{% static 'myapp/js/main.js' %}"></script>
```

* Always put `{% load static %}` at the top (before using `{% static %}`).
* The path inside `{% static '...' %}` is relative to any `static/` directories Django knows.

#### 🔧 During Development

* `python manage.py runserver` will serve static automatically if `DEBUG=True`.
* Visit pages; browser will request `/static/myapp/css/styles.css`, and Django serves it.

#### 🔧 Preparing for Production (Overview)

* Set `DEBUG=False` and configure `STATIC_ROOT` (e.g., `staticfiles/`).
* Run:

  ```bash
  python manage.py collectstatic
  ```

  * This collects all static assets into `STATIC_ROOT`.
* Configure your web server (e.g., Nginx) to serve `/static/` from that directory. (We’ll cover deployment later.)

---

### 3. Template Inheritance + Static: Putting It Together

1. **Create base.html** with links to your CSS/JS via `{% static %}`.
2. **Extend base.html** in child templates.
3. **Place static assets** in proper `static/` directories.
4. **Check in browser**: Inspect network tab to ensure CSS/JS are loading.

---

### 4. Common Pitfalls & Tips

* **Forgetting `{% load static %}`** → `{% static ... %}` tag won’t work.
* **Wrong path inside `{% static %}`**: Ensure correct namespace (e.g., `'myapp/css/styles.css'`).
* **Not adding app to `INSTALLED_APPS`**: Django won’t look into its `static/` folder.
* **Cached old CSS**: When you change CSS, clear browser cache or use cache-busting techniques (e.g., add version query param during development).
* **Missing trailing slash** vs no slash in URLs: For `path()` patterns, ensure consistency (e.g., `path('about/', ...)`). For static links, `{% static %}` builds correct path.
* **Static files in templates vs. static files for admin**: Admin has its own static; Django handles it automatically.

