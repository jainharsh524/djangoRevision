# 🧩 Chapter 4: Django Templates — Rendering HTML Pages


## 🧩 What is `render()` in Django?

```python
from django.shortcuts import render
```

The `render()` function is a **shortcut** provided by Django that:

1. **Combines** a given template with a **context dictionary**.
2. **Returns** an `HttpResponse` with that rendered text (HTML).

---

### 🛠️ Syntax

```python
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

Let’s break it down:

| Parameter       | Description                                                              |
| --------------- | ------------------------------------------------------------------------ |
| `request`       | Mandatory. The HTTP request object.                                      |
| `template_name` | Mandatory. The name (or path) of the HTML template.                      |
| `context`       | Optional. A Python dictionary with variables passed into the template.   |
| `content_type`  | Optional. Default is `'text/html'`.                                      |
| `status`        | Optional. HTTP status code (like `200`, `404`, etc.).                    |
| `using`         | Optional. Which **template engine** to use (if multiple are configured). |

---

### ✅ Example

#### `views.py`

```python
def dashboard(request):
    user_info = {
        'name': 'Harsh',
        'points': 80
    }
    return render(request, 'dashboard.html', user_info)
```

#### `dashboard.html`

```html
<h1>Welcome {{ name }}</h1>
<p>You have {{ points }} points!</p>
```

> The `render()` call converts the `dashboard.html` template into final HTML using the `user_info` dictionary and sends it back as an `HttpResponse`.

---

## 🧠 What Actually Happens?

```python
return render(request, 'home.html', {'name': 'Harsh'})
```

🔁 Behind the scenes:

1. Django **loads the template** `home.html`.
2. **Injects the context** `{'name': 'Harsh'}` into it using the template engine.
3. Generates a final **HTML string** like:

   ```html
   <h1>Hello Harsh</h1>
   ```
4. Returns it wrapped inside an `HttpResponse` object like:

   ```python
   return HttpResponse("<h1>Hello Harsh</h1>")
   ```

---

## 🚀 Bonus: `render()` vs `HttpResponse`

| Task                    | `HttpResponse` | `render()`                       |
| ----------------------- | -------------- | -------------------------------- |
| Manual string writing   | ✅              | ❌ (not needed)                   |
| Use of template files   | ❌              | ✅ (preferred for HTML)           |
| Supports template logic | ❌              | ✅ (supports `{% %}` and `{{ }}`) |
| Return HTML             | ✅              | ✅                                |

Great, Harsh! Let's move to **Chapter 4: Templates in Django** — one of the most important parts of building real websites.


---

## 🟢 What is a Template?

A **template** is an HTML file where we embed **dynamic content** using Django's template language.

Instead of sending plain text with `HttpResponse`, we render a `.html` file using `render()`.

---

### ✅ Basic View Without Template:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Harsh!")
```

---

### ✅ Now Using a Template:

#### Step 1: Create Template Directory

Inside your app folder (e.g. `myapp/`):

```
myapp/
├── views.py
├── templates/
│   └── home.html
```

> Create the `templates` folder if not already there.

#### Step 2: Sample `home.html`

```html
<!-- myapp/templates/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Django Home</title>
</head>
<body>
    <h1>Hello {{ name }}!</h1>
</body>
</html>
```

---

#### Step 3: Update View with `render()`

```python
from django.shortcuts import render

def home(request):
    context = {'name': 'Harsh'}
    return render(request, 'home.html', context)
```

---

## 🛠️ Template Syntax Basics

| Task              | Syntax                                    |
| ----------------- | ----------------------------------------- |
| Output a variable | `{{ variable }}`                          |
| For loop          | `{% for item in list %} ... {% endfor %}` |
| If condition      | `{% if user %} ... {% endif %}`           |
| Comments          | `{# This is a comment #}`                 |
| Include file      | `{% include "file.html" %}`               |

---

## ✅ Example: Loop in Template

```html
<ul>
  {% for fruit in fruits %}
    <li>{{ fruit }}</li>
  {% endfor %}
</ul>
```

And in your `views.py`:

```python
def home(request):
    context = {'fruits': ['Apple', 'Banana', 'Cherry']}
    return render(request, 'home.html', context)
```

---

## 🎯 Summary

* Templates help you return **HTML with dynamic data**.
* Stored in `templates/` folder.
* Use `render(request, 'file.html', context)` to serve them.
* Use `{{ variable }}` and `{% %}` tags in your HTML.