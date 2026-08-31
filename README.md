# Django Blogging System

A full-featured blog publishing platform built with Django. It provides a public-facing blog with categories, featured posts, search, and comments, along with an admin dashboard for managing posts, categories, and users.

## Features

- **Homepage** — Hero section with featured posts, recent articles, and a sidebar with "About Us" info and social media links
- **Category Navigation** — Dynamic category bar; filter posts by category
- **Blog Posts** — Create, edit, and publish posts with featured images, short descriptions, and rich body content
- **Featured Posts** — Flag posts as featured for homepage hero treatment
- **Comments System** — Authenticated users can comment on blog posts
- **Search** — Full-text search across post titles, descriptions, and body content
- **User Authentication** — Registration, login, and logout
- **Admin Dashboard** — Manage categories, posts, and users with full CRUD operations
- **User Management** — Add, edit, and delete users (permission-gated)
- **Custom 404 Page** — Styled error page for not-found requests

## Tech Stack

- **Backend:** Python 3.14, Django 6.1
- **Frontend:** Bootstrap 5, Bootstrap 4 (forms via crispy-forms), Font Awesome, Google Fonts
- **Database:** SQLite3
- **Image Processing:** Pillow

## Project Structure

```
django-blogging-system/
├── Blog/
│   ├── manage.py
│   ├── requirements.txt
│   ├── blog_main/          # Project config, auth views, settings
│   ├── blogs/              # Core blog app (posts, categories, comments)
│   ├── dashboard/          # Admin dashboard (CRUD for posts/categories/users)
│   ├── About/              # About page and social links
│   ├── templates/          # All HTML templates
│   ├── static/             # CSS and static assets
│   └── media/              # Uploaded images
└── README.md
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/django-blogging-system.git
   cd django-blogging-system/Blog
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv env

   # Windows
   env\Scripts\activate

   # macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin/dashboard access)

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Open** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser

> **Note:** `DEBUG` is set to `False` in settings. For local development, set `DEBUG = True` in `Blog/blog_main/settings.py` or add `127.0.0.1` to `ALLOWED_HOSTS`.

## Usage

| URL | Description |
|---|---|
| `/` | Homepage with featured and recent posts |
| `/category/<id>/` | Posts filtered by category |
| `/blogs/<slug>/` | Single blog post with comments |
| `/blogs/search/` | Search posts |
| `/login/` | User login |
| `/register/` | User registration |
| `/dashboard/` | Admin dashboard (login required) |

## License

This project is open source and available for personal and educational use.