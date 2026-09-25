# Study Planner (Beginner Project) — Python + Django + MySQL

A simple app to add subjects and study tasks, mark tasks done, and see them
in one list. Built to be easy to read and extend if you're learning Django.

## 1. Create the MySQL database

Open the MySQL shell (`mysql -u root -p`) and run:

```sql
CREATE DATABASE study_planner;
CREATE USER 'planner_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON study_planner.* TO 'planner_user'@'localhost';
FLUSH PRIVILEGES;
```

(Change `password123` to your own password, and use the same one in step 3.)

## 2. Install requirements

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

If `mysqlclient` fails to install:
- Ubuntu/Debian: `sudo apt install python3-dev default-libmysqlclient-dev build-essential`
- macOS: `brew install mysql pkg-config`

## 3. Set your database password

Open `studyplanner_project/settings.py` and find the `DATABASES` section near
the bottom. Put your MySQL username and password there.

## 4. Create the tables and run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   # optional, lets you use /admin/
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## What's inside

- **One app** called `studyplanner` — everything lives in it, which is normal
  for a small beginner project.
- **Two models**: `Subject` (e.g. "Maths") and `Task` (e.g. "Finish chapter 4",
  linked to a subject, with a due date and a done checkbox).
- **Function-based views** (not class-based) in `views.py` — easier to read
  when you're starting out.
- **No user accounts** — every task is shared, like a shared to-do list. This
  keeps the first version simple. Adding logins is a good next step once
  you're comfortable with this.

## Next things to try adding yourself

- User accounts, so each person has their own tasks (`django.contrib.auth`).
- Priority levels (low/medium/high) on a task.
- Sorting tasks by due date automatically (already done — see `Meta.ordering`
  in `models.py` — try changing it).
- A search box.
