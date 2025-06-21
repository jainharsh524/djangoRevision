`{% extends %}` and `{% include %}` are both used in Django templates, but they serve **very different purposes**.

---

## 🔁 `{% extends 'base.html' %}`

### ✅ Purpose:

To **inherit** the layout of a parent template (`base.html`), and override specific parts of it using **template blocks**.

### ✅ Usage:

Used when you want to build **a full page** based on a layout defined in `base.html`.

### ✅ Example:

```html
<!-- about.html -->
{% extends 'base.html' %}

{% block title %}About Us{% endblock %}

{% block content %}
  <h2>About Page</h2>
  <p>This content goes into the content block of base.html.</p>
{% endblock %}
```

This works with `base.html` like:

```html
<!-- base.html -->
<html>
<head>
  <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

📌 It creates a **parent-child relationship**. The child overrides the blocks defined by the parent.

---

## 📥 `{% include 'base.html' %}`

### ✅ Purpose:

To **insert** the contents of another template (like a reusable header, footer, navbar) **inside the current template** — like a copy-paste.

### ✅ Usage:

Used for including **partial templates** (components) inside another template.

### ✅ Example:

```html
<!-- home.html -->
<html>
  <body>
    {% include 'navbar.html' %}
    <h1>Welcome to the homepage!</h1>
    {% include 'footer.html' %}
  </body>
</html>
```

`navbar.html`:

```html
<nav>
  <a href="/">Home</a>
  <a href="/about/">About</a>
</nav>
```

📌 It does **not use block structure**. It simply **inserts** the HTML wherever the tag is placed.

---

## ⚖️ Summary of Differences

| Feature              | `{% extends %}`              | `{% include %}`                       |
| -------------------- | ---------------------------- | ------------------------------------- |
| Purpose              | Template Inheritance         | Reusable Template Insertion           |
| Relationship         | Parent–Child Template        | No relationship                       |
| Use Case             | Full-page layout inheritance | Including partials like navbar/footer |
| Uses `{% block %}`   | ✅ Yes                        | ❌ No                                  |
| Reusability Level    | High-level structure         | Low-level components                  |
| Can override content | ✅ Yes, with `{% block %}`    | ❌ No                                  |
