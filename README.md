# 🎓 Campus Lost & Found System

A web-based Campus Lost & Found System built with Django. The application allows students and campus members to report lost or found items and manage their reports through a simple web interface.

---

## 🚀 Project Overview

The Campus Lost & Found System is a Django-based web application designed to make it easier for students to report and find lost items within a campus environment.

This project is being developed as a practical Django learning project with a focus on building real-world application features.

### Core Django Concepts

- Django Forms
- Django Templates
- CRUD Operations
- User Authentication
- Django ORM
- Custom Middleware
- Django Messages Framework
- File/Image Upload
- User-based Permissions

---

## ✨ Features

### 🔐 Authentication

- User Registration
- User Login
- User Logout
- Authenticated report creation
- Each report belongs to the user who created it

### 📝 Lost & Found Reports

Users can create reports containing:

- Item Name
- Report Type (Lost / Found)
- Category
- Description
- Location
- Date
- Contact Information
- Item Image
- Report Status

### 📋 Report Management

Planned functionality includes:

- View all reports
- View individual report details
- Edit own reports
- Delete own reports
- Mark own reports as resolved
- View personal reports

### 🔎 Search & Filtering

Users will be able to:

- Search by item name
- Filter by report type
- Filter by category
- Filter by status
- Combine multiple filters

### 🛡️ Access Control

Users will only be allowed to modify or delete their own reports.

### ⚙️ Middleware

Custom middleware will be used to log request information such as:

- User
- HTTP Method
- Request Path
- Request Time

### 💬 Messages

Django's Messages Framework will provide feedback for actions such as:

- Report creation
- Report update
- Report deletion
- Report resolution
- Login
- Logout

---

## 🛠️ Technologies Used

- **Python**
- **Django**
- **SQLite**
- **HTML5**
- **CSS3**
- **Django Templates**
- **Django ORM**
- **Git**
- **GitHub**

---

## 📁 Project Structure

```text
Assignment8/
│
├── campus_lost_found/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── reports/
│   ├── migrations/
│   ├── templates/
│   │   └── reports/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── report_form.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── manage.py
└── README.md
```
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/showmanme/campus-lost-found-system.git
2. Navigate to the Project
cd campus-lost-found-system
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment
Windows PowerShell
venv\Scripts\Activate.ps1
5. Install Dependencies

Install Django:

pip install django

Install Pillow for image uploads:

pip install pillow
6. Apply Database Migrations
python manage.py migrate
7. Create a Superuser
python manage.py createsuperuser

Follow the instructions shown in the terminal.

8. Start the Development Server
python manage.py runserver

Open the application at:

http://127.0.0.1:8000/

🔐 Authentication

The application uses Django's built-in authentication system.

Users can:

Register an account
Login
Create reports while authenticated
Logout

Each report is connected to the user who created it.

User
 │
 ├── Report
 ├── Report
 └── Report
📦 Report Model

Each lost or found report contains information about the item.

The main fields include:

Owner
Item Name
Report Type
Category
Description
Location
Date
Contact Information
Image
Status
Created At
Updated At

The report status can be:

Active
Resolved
🗄️ Database

The project uses SQLite during development and Django's Object-Relational Mapper (ORM) for database operations.

The Django ORM allows the application to interact with database records using Python objects and QuerySets.

The basic relationship is:

User
 │
 │ owns
 ▼
Report

This relationship allows the application to determine which reports belong to a particular user.

🧪 Testing

Run Django's system checks:

python manage.py check

Run the project's tests:

python manage.py test
📌 Project Status

🚧 Currently in Development

Completed
Django project setup
Reports application
Report model
Database migrations
Django Admin registration
User registration
User login
User logout
Authentication protection
Report creation form
Image upload support
Basic report creation functionality
In Progress / Planned
Report listing
Report details
Update reports
Delete reports
Mark reports as resolved
Search functionality
Filtering
My Reports page
Custom middleware
Improved message handling
Template inheritance
Responsive UI
CSS styling
Final testing
Deployment
🎯 Learning Objectives

The main goal of this project is to strengthen practical Django development skills by building a real-world application from the ground up.

The project demonstrates how different Django components work together:

User
  ↓
URL
  ↓
View
  ↓
Form
  ↓
Model
  ↓
Database
  ↓
Template
  ↓
User

The project also provides practical experience with:

Authentication
Authorization
CRUD operations
Database relationships
Django Forms
File uploads
Middleware
Server-side validation
Template rendering
🔄 Application Flow

A typical report creation process works like this:

User Login
    ↓
Report Form
    ↓
Submit Report
    ↓
Django Form Validation
    ↓
Create Report Object
    ↓
Assign Logged-in User as Owner
    ↓
Save to Database
    ↓
Success Message
    ↓
Redirect
👨‍💻 Author
Rahimur Rahman Showrav

B.Sc. in Computer Science & Engineering

⭐ Project Goal

This project is part of a continuous learning journey focused on developing practical full-stack web development skills using Django and related technologies.

The application will be progressively improved with additional functionality, better UI/UX, security, testing, and deployment.
