# payment_app


### Installation
***
#### To set up the project locally, follow these steps:
- Clone the repository:
```
git clone https://github.com/your-username/toraaglobal.git
cd toraaglobal
```

- Create a virtual environment:
```
python3 -m venv env
source env/bin/activate
```

- Install dependencies:
```
pip install -r requirements.txt
```

- Apply migrations:
```
python manage.py migrate
```

- Run the development server:
```
python manage.py runserver
```

The website should now be accessible at http://127.0.0.1:8000/.

### Deployment on Railway
Railway is a platform that allows you to deploy applications with ease. Follow these steps to deploy the Toraaglobal website on Railway:

- Sign Up/Log In to Railway: If you don't already have an account, sign up at Railway.

- Create a New Project:

    - After logging in, click on "New Project" from the dashboard.
    - Select "Deploy from GitHub repo" and connect your GitHub account if you haven't done so already.
    - Choose the Toraaglobal repository from your list of repositories.


- Configure Environment Variables:
    - Railway will automatically detect your requirements.txt and manage.py file.
    - Set up the following environment variables in the Railway dashboard:
        - DJANGO_SECRET_KEY: Your Django secret key.
        - DATABASE_URL: The URL of your PostgreSQL database.
        - DEBUG: Set to False for production.
    - You may also need to add any other environment variables your project depends on, such as ALLOWED_HOSTS, STATIC_URL, etc.

- Deployment Settings:
Railway will handle the deployment automatically. Ensure your Procfile is set up to run Django migrations and start the application:
```
release: python manage.py migrate
web: gunicorn main.wsgi
```

- Deploy the Project:
    - Once everything is configured, click "Deploy" to start the deployment process.
    - After deployment, you can access your site via the domain provided by Railway, or you can set up a custom domain (e.g., www.toraaglobal.com).

- Monitor and Manage:
Railway provides logs and metrics to help you monitor the performance of your site. Use these tools to ensure everything is running smoothly.