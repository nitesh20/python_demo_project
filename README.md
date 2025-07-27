# Django Role-Based Access Control (RBAC) Project

This is a Django-based project implementing Role-Based Access Control (RBAC) with user authentication, permissions, and role management.

## 📁 Project Structure

demoproject/ # Main Django project settings
rolebase/ # App for handling roles and permissions and auth
task/ # App for task-related functionality
venv/ # Python virtual environment (excluded via .gitignore)
manage.py # Django CLI entry point

** Features

- JWT Authentication
- Roles: Admin, Manager, User (customizable)
- Custom Django permissions
- Modular Django apps

## 🛠️ Setup Instructions

# 1. Clone the Repository

```bash
git clone https://github.com/nitesh20/python_demo_project.git
cd demoproject

# 1. Clone the Repository
```bash
git clone https://github.com/nitesh20/python_demo_project.git
cd demoproject

# 2 Create venv (if not already)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3 Install dependencies
pip install -r requirements.txt

# 4 Run migrations command
python manage.py makemigrations
python manage.py migrate

# 5 Start the Server
python manage.py runserver

### Role Logics

there are 3 role in projects

1 - Admin 
2 - Manager
3 - User

1 - Admin Intro
=> admin can do call the things like. registration, create update and delete user

2 - Manager Intro
=> Manager can manage all the data of user under them.

3 - User Intro
=> User can only show their own data only. and they can update only


### API LIST

1 - Registration of User
http://localhost:8000/api/register/

2 - Login User
http://localhost:8000/api/token/

3 - User list display according Role
http://localhost:8000/api/user/

4 - add task
http://localhost:8000/api/task/

5 - list of task
http://localhost:8000/api/task/list

6 - update task
http://localhost:8000/api/task/3/

7 - delete task
http://localhost:8000/api/task/3/


#### Access by user

user credentials:
  admin Users
  admin admin123

  managers Users
  nitesh nit@1234
  vivek  viv@1234

  users
  amit ami@1234
  rahul rah@1234
  ashish ash@1234
  ajit aji@1234
  adarsh ada@1234
  muskan mus@1234
  aditya adi@1234
  Sumit  sum@1234

