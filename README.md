# 📘 Job Board — Project Setup & Run Guide

A complete guide to install, configure, and run the **Django Job Board** project locally.  
This document is designed for developers, evaluators, and teammates who need a clear and reliable onboarding experience.

---

## 🚀 Overview

This project is a modular Django application composed of multiple apps:

- **accounts** — authentication, registration, login  
- **company** — company profiles  
- **jobListings** — job posting system  
- **applicationPipeline** — application workflow, status rules, services  
- **search** — job and company search  
- **projeto_jobBoard** — main Django project (settings, URLs, templates, static)

The project uses **SQLite**, **Django**, and a clean folder structure with templates and static files.

---

## 📦 1. Requirements

### **System Requirements**
- Python **3.11+**
- SQLite (bundled with Python)
- Git (optional)

### **Python Dependencies**
The project uses `pyproject.toml` and `uv.lock`.

You can install dependencies using:

#### **Option A — uv (recommended)**
```bash
pip install uv

🛠️ 2. Install Dependencies
---------------------------

### Using **uv**

bash

```
uv sync

```

### Using **pip**

Install Django manually:

bash

```
pip install django

```

Or, if you generate a `requirements.txt`:

bash

```
pip install -r requirements.txt

```

⚙️ 3. Environment Setup
-----------------------

This project does **not** require environment variables by default. If you later add email services, API keys, or secrets, document them here.

🗄️ 4. Database Setup
---------------------

The repository already includes:

Código

```
db.sqlite3

```

To ensure migrations are applied:

bash

```
python manage.py migrate

```

To create an admin user:

bash

```
python manage.py createsuperuser

```

▶️ 5. Running the Project
-------------------------

From the project root:

bash

```
python manage.py runserver

```

Then open:

Código

```
http://127.0.0.1:8000/

```

🧩 6. Project Structure
-----------------------

Código

```
.
├── accounts/                 # User authentication
├── applicationPipeline/      # Application workflow + services
├── company/                  # Company profiles
├── jobListings/              # Job posting system
├── search/                   # Search functionality
├── projeto_jobBoard/         # Main Django project
│   ├── settings.py
│   ├── urls.py
│   ├── templates/base.html
│   └── static/style.css
├── db.sqlite3                # SQLite database
├── manage.py                 # Django CLI entrypoint
├── pyproject.toml            # Dependency configuration
├── uv.lock                   # Dependency lockfile
└── makefile                  # Optional automation commands

```

🧪 7. Running Tests
-------------------

Each app includes a `tests.py`. Run all tests with:

bash

```
python manage.py test

```

🧹 8. Optional: Using the Makefile
----------------------------------

If your Makefile includes shortcuts, common commands might be:

bash

```
make run
make migrate
make superuser

```

Check the file to confirm available targets.

🌐 9. Static Files
------------------

To collect static files (for deployment):

bash

```
python manage.py collectstatic

```

🧭 10. URL Routing
------------------

Each app has its own `urls.py`, included in:

Código

```
projeto_jobBoard/urls.py

```

This keeps routing modular and clean.

🎨 11. Templates
----------------

Each app contains its own template directory:

Código

```
accounts/templates/accounts/
jobListings/templates/jobListings/
company/templates/company/
applicationPipeline/templates/applicationPipeline/
search/templates/search/

```

Global layout:

Código

```
projeto_jobBoard/templates/base.html

```

🧰 12. Services Layer
---------------------

The `applicationPipeline` app includes a dedicated services folder:

Código

```
services/
    applications_service.py
    status_rules.py
```