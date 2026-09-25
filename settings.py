"""
Django settings for studyplanner_project.
This is a BEGINNER-friendly settings file: values are written directly here
instead of being read from environment variables, so you can see exactly
what's being configured. For a real project you would keep secrets like
SECRET_KEY and the database password out of the code instead.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Security --------------------------------------------------------------
# In a real project, generate your own secret key and never share it.
SECRET_KEY = "django-insecure-change-this-key-before-you-deploy-anywhere"

DEBUG = True  # Shows helpful error pages. Turn this OFF before going live.

ALLOWED_HOSTS = []  # Fine to leave empty while DEBUG = True.

# --- Apps --------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "studyplanner",  # our app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "studyplanner_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,  # lets Django find templates inside studyplanner/templates/
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "studyplanner_project.wsgi.application"

# --- Database: MySQL ---------------------------------------------------------
# Fill in YOUR username and password below (see README step 3).
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "study_planner",
        "USER": "planner_user",
        "PASSWORD": "password123",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

# --- Passwords -----------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Internationalization -----------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --- Static files (CSS) ---------------------------------------------------
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
