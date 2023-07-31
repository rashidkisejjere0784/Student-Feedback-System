# Student Feedback System - Django Soft Dashboard

The Student Feedback System is an open-source Django project built on top of the Soft Dashboard, an open-source Bootstrap 5 design from Creative-Tim. It is designed for those who appreciate bold elements and beautiful websites, providing a wide range of elements, designed blocks, and fully coded pages to create stunning websites and web apps.

## Features

- ✅ Up-to-date Dependencies
- ✅ Theme: [Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard), designed by Creative-Tim
  - Can be used in any Django project (new or legacy)
- ✅ Authentication: Django.contrib.AUTH, Registration
- 🚀 Deployment
  - CI/CD flow via Render
  - [Django Soft - Go LIVE](https://www.youtube.com/watch?v=1QVdQVSkUCI) - Video presentation

### Useful Links

- [Django Soft Dashboard - Product page](https://appseed.us/product/soft-ui-dashboard/django/)
- [Django Soft Dashboard - LIVE Demo](https://django-soft-dash.onrender.com)
- 🛒 [Django Soft Dashboard PRO - Premium Version](https://appseed.us/product/soft-ui-dashboard-pro/django/)

## Manual Build

To set up the Student Feedback System manually, follow these steps:

1. **Download the code**

   ```bash
   $ git clone https://github.com/app-generator/django-soft-ui-dashboard.git
   $ cd django-soft-ui-dashboard
    ```
    ---
2. Install modules `via VENV`
    ```bash
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    ```
    ---
   
3. Set Up Database
   ```bash
   $ python manage.py makemigrations
    $ python manage.py migrate
   ```
   ---
   
4. Create the Superuser
```bash
$ python manage.py createsuperuser
```
5. Start the app
```bash
$ python manage.py runserver
```
The app will run at `http://127.0.0.1:8000/.`
---

## Codebase Structure
The project follows a simple and intuitive structure:
```bash
< PROJECT ROOT >
   |
   |-- core/
   |    |-- settings.py   # Project Configuration
   |    |-- urls.py       # Project Routing
   |
   |-- home/
   |    |-- views.py      # APP Views
   |    |-- urls.py       # APP Routing
   |    |-- models.py     # APP Models
   |    |-- tests.py      # Tests
   |
   |-- templates/
   |    |-- includes/     # UI components
   |    |-- layouts/      # Masterpages
   |    |-- pages/        # Kit pages
   |
   |-- static/
   |    |-- css/          # CSS Files
   |    |-- scss/         # SCSS Files
   |         |-- soft-ui-dashboard/_variables.scss # File Used for Theme Styling
   |
   |-- requirements.txt   # Project Dependencies
   |
   |-- env.sample         # ENV Configuration (default values)
   |-- manage.py          # Start the app - Django default start script
   |
   |-- ************************************************************************
```
--- 
## Recompile SCSS  

The SCSS/CSS files used to style the UI are saved in the `static` directory. 
In order to update the UI colors (primary, secondary) this procedure needs to be followed. 

```bash
$ yarn                                             # install modules
$ vi static/scss/soft-ui-dashboard/_variables.scss # edit variables 
$ gulp                                             # SCSS to CSS translation
```
