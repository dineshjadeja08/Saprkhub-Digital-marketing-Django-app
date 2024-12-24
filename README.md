<<<<<<< HEAD
# Saprkhub Digital marketing Django app
 
 
=======
# SparkHub Digital Marketing Django App

This is a Django-based application for digital marketing. Follow the steps below to set up and run the project on your local machine.

## Prerequisites

Ensure that you have the following installed on your machine:
- Python (3.10 or above)
- pip (Python package manager)
- Virtual Environment (optional but recommended)

## Steps to Run the Project

### 1. Clone the Repository

If you haven't cloned the repository yet, run the following command in your terminal to clone the project:

```bash
git clone <your-repository-url>
cd Saprkhub-Digital-marketing-Django-app
2. Create a Virtual Environment (optional but recommended)
To avoid version conflicts, it's recommended to create a virtual environment. You can do this with the following commands:

For Windows:

bash
Copy code
python -m venv venv
venv\Scripts\activate
For macOS/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required Python packages for the project using pip:

bash
Copy code
pip install -r requirements.txt
If the requirements.txt file is not present, you can install the core dependencies manually:

bash
Copy code
pip install django
pip install django-allauth
4. Set Up the Database
Run the following command to apply any database migrations:

bash
Copy code
python manage.py migrate
5. Install django-allauth (if not already installed)
If you haven't installed django-allauth, run:

bash
Copy code
pip install django-allauth
Ensure that you have added allauth to your INSTALLED_APPS in settings.py:

python
Copy code
INSTALLED_APPS = [
    # other apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
6. Set Up Static Files (Optional)
To serve static files in development, run:

bash
Copy code
python manage.py collectstatic
7. Run the Development Server
Finally, start the Django development server:

bash
Copy code
python manage.py runserver
By default, the server will run at http://127.0.0.1:8000/. Open this URL in your browser to see the application in action.

8. Create a Superuser (Optional)
If you want to log in to the Django admin panel, create a superuser:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up the superuser.

9. Access the Django Admin Panel
After running the server, you can access the Django Admin Panel at:

arduino
Copy code
http://127.0.0.1:8000/admin
Log in using the superuser credentials you created.

Troubleshooting
ModuleNotFoundError: No module named 'allauth'
If you encounter this error, make sure you have installed django-allauth by running pip install django-allauth.

Database Configuration Errors
If you're using SQLite as the database, make sure the DATABASES setting in settings.py is correctly configured:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


License
This project is licensed under the MIT License.


Feel free to adjust it to your project specifics, especially if you have any other custom s
Screen schots 
Home page---
![image](https://github.com/user-attachments/assets/a7775d78-f1a8-4805-bcab-60f231999b24)
Sign in page ---
![image](https://github.com/user-attachments/assets/eb2b32c0-4e87-4dd9-8f3e-7c95bdbd5d4e)
Sign up page ---
![image](https://github.com/user-attachments/assets/8b144647-ff3f-4f6e-b57e-6d9e314cd617)
Dashboard ----
![image](https://github.com/user-attachments/assets/8512cb25-887f-40c4-86fd-2a8a13cecaf4)
Create a campaign----
![image](https://github.com/user-attachments/assets/a1fb9c05-57e6-47b0-a694-f7d039564d0e)
Logout page----
![image](https://github.com/user-attachments/assets/b5eb62bd-4fb7-4298-b940-d212d3429a64)

