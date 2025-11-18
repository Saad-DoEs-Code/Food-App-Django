# 🍽️ FoodBox

### **User-Owned Item Listing Platform (Django)**

FoodBox is a foundational Django web application demonstrating user authentication, CRUD operations, database relationships, signals, media uploads, and both Class-Based and Function-Based Views.

Authenticated users can list food items, browse items created by others, and manage their own listings.

---

## ✨ Features

### **1. 🔐 User Management**

* **Custom Registration Form** (`users/forms.py`)
* Django’s built-in `LoginView` & `LogoutView`
* **Profile Model** linked with Django’s User (OneToOneField)
* Auto-profile creation using **Signals** (`post_save`)
* Avatar upload via `ImageField`

---

### **2. 🍔 Food Item Management**

* Each item linked to its creator via a **ForeignKey**
* Full CRUD:

  * **Create** → `CreateView` (auto-assign logged-in user)
  * **Read** → `ListView` + `DetailView`
  * **Update/Delete** → FBVs (`update_item`, `delete_item`)
* Uses Django messages for user-friendly feedback

---

### **3. 🎨 Frontend & Templates**

* Template inheritance with `base.html`
* Clean and responsive UI with **Bootstrap 5**
* Media support for profile images

---

## 🛠️ Concepts Demonstrated

* Models (OneToOneField, ForeignKey, get_absolute_url)
* Class-Based Views + Function-Based Views
* Django Signals (automatic profile creation)
* Custom and ModelForms
* Namespaced URLs with `include()`
* Media + static file handling

---

## 📁 Project Structure (Sample)

```
FoodBox/
│
├── items/
├── users/
├── templates/
├── static/
├── media/
│
├── FoodBox/        # Main project folder
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
└── manage.py
```

---

# 🚀 Deployment Guide

This README now includes full instructions for deploying to:

* **Vercel (via Django + ASGI + Serverless)**
* **Render (recommended for Django beginners)**

---

# 🌐 Deployment on Render (RECOMMENDED)

Render is the easiest option because Django runs normally (not serverless).

### **1. Create a GitHub repo & push your project**

```
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### **2. Go to Render Dashboard**

👉 [https://dashboard.render.com/](https://dashboard.render.com/)

### **3. Create a new Web Service**

* **Runtime:** Python
* **Build Command:**

  ```
  pip install -r requirements.txt
  python manage.py collectstatic --noinput
  ```
* **Start Command:**

  ```
  gunicorn FoodBox.wsgi:application
  ```

### **4. Add Environment Variables**

Go to **Environment → Add Environment Variables**:

| Variable        | Value                                  |
| --------------- | -------------------------------------- |
| `SECRET_KEY`    | your-secret-key                        |
| `DEBUG`         | False                                  |
| `ALLOWED_HOSTS` | your-render-url.onrender.com           |
| `DATABASE_URL`  | (Render auto-adds if using PostgreSQL) |

### **5. Configure Static & Media**

Modify `settings.py`:

```python
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
```

### **6. Deploy**

Render will build → migrate → start server.

Done! 🎉

---

# ▲ Deployment on Vercel (ADVANCED)

Vercel is optimized for Node/Next.js — Django needs workarounds.
We deploy Django using **Vercel Serverless** + **ASGI adapter**.

### **1. Install Required Packages**

```
pip install gunicorn whitenoise django-environ uvicorn
```

### **2. Add `vercel.json`**

Create at project root:

```json
{
  "builds": [
    {
      "src": "FoodBox/asgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "FoodBox/asgi.py"
    }
  ]
}
```

### **3. Update `settings.py`**

Inside `settings.py`:

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
```

### **4. Add `asgi.py`**

(If not already present)

```python
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FoodBox.settings")

application = get_asgi_application()
```

### **5. Deploy**

Install Vercel CLI:

```
npm i -g vercel
vercel login
vercel
```

Follow prompts → select your repo → deploy.

⚠ **Limitations on Vercel**

* No persistent local disk → media uploads require AWS S3 or Cloudinary
* Cold starts may delay responses
* Some Django packages may not behave well in serverless environments

For beginners, **Render is strongly recommended**.

---

# 🧪 Local Development

### **Install Dependencies**

```
pip install -r requirements.txt
```

### **Run Server**

```
python manage.py migrate
python manage.py runserver
```

### **Create Superuser**

```
python manage.py createsuperuser
```

---


