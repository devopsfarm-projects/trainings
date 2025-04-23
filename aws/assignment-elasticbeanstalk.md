AWS Elastic Beanstalk Deployment for a Django Application

Problem Statement:

Your task is to deploy a simple, functional Python Django web application to the AWS Elastic Beanstalk service. This exercise will familiarize you with the process of packaging a Django application, configuring an Elastic Beanstalk environment, and monitoring its deployment and health. You will learn how Elastic Beanstalk simplifies the infrastructure management required to run web applications in the AWS cloud.

Steps:

    Set Up Your Local Django Application:
        Ensure you have Python and pip installed on your local machine.
        Create a new Django project named mydjangoapp:
        Bash

django-admin startproject mydjangoapp
cd mydjangoapp

Create a simple Django app within the project, for example, named hello:
Bash

python manage.py startapp hello

In the hello/views.py file, create a simple view:
Python

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from Django on Elastic Beanstalk!")

In the hello/urls.py file, define a URL pattern for the index view:
Python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

Include the hello app's URLs in the main mydjangoapp/urls.py file:
Python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),
]

Make initial migrations and create a superuser (though not strictly necessary for this basic deployment, it's good practice):
Bash

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Test your local development server to ensure the app runs correctly:
Bash

    python manage.py runserver 0.0.0.0:8000

    Open your web browser and navigate to http://localhost:8000/. You should see "Hello from Django on Elastic Beanstalk!".

Prepare Your Application for Elastic Beanstalk:

    Create a requirements.txt file: This file lists the Python dependencies for your project. In your project's root directory (mydjangoapp), run:
    Bash

        pip freeze > requirements.txt

        Create a Procfile: Elastic Beanstalk needs a Procfile in the root of your application bundle to know how to run your application. Create a file named Procfile (without any extension) with the following content:

        web: gunicorn mydjangoapp.wsgi --bind :8000

        (This assumes you have gunicorn installed. If not, add it to your requirements.txt and install it locally.)
        Optional: Configure Static Files: For a more robust application, you would typically configure Django to serve static files correctly. While not strictly required for this basic exercise, be aware that for production deployments, you'll need to handle static files (e.g., using WhiteNoise or a CDN).

    Package Your Application:
        Create a ZIP archive of your Django project. Ensure that the manage.py file and the requirements.txt and Procfile are at the root of the ZIP file. You can typically achieve this by navigating to the directory containing the mydjangoapp folder and then zipping the mydjangoapp folder and the requirements.txt and Procfile files. Alternatively, navigate into the mydjangoapp directory and zip all the contents within it, along with the requirements.txt and Procfile which should be one level up. The latter approach is generally recommended.

    Deploy to AWS Elastic Beanstalk:
        Access the AWS Management Console: Log in to your AWS account and navigate to the Elastic Beanstalk service.
        Create a New Application: Click on "Create Application". Give your application a name (e.g., django-eb-app).
        Create a New Environment: Within your application, click "Create environment".
        Choose Environment Tier: Select "Web server environment".
        Configure Environment:
            Give your environment a name (e.g., django-env).
            For "Platform", select "Python" and choose a recent Python version that is compatible with your application.
            For "Application code", choose "Upload your code". Upload the ZIP file you created in the previous step.
            You can leave the other configuration options as default for this basic deployment. However, in a real-world scenario, you would configure instance types, security groups, database integration, etc.
        Review and Create: Review your environment configuration and click "Create environment". AWS will now provision the necessary resources and deploy your application. This process may take several minutes.

    Monitor Your Deployment:
        Once the environment is created, Elastic Beanstalk will display the environment's health status. Wait until the status turns "OK".
        Click on the environment's URL provided by Elastic Beanstalk. This will open your deployed Django application in a new browser tab. You should see the "Hello from Django on Elastic Beanstalk!" message.
        Explore the Elastic Beanstalk dashboard for your environment. Observe the health status, events, logs, and configuration details.

    Clean Up (Important):
        To avoid incurring unnecessary AWS charges, once you have completed the assignment, terminate your Elastic Beanstalk environment. In the Elastic Beanstalk console, select your environment and choose "Actions" -> "Terminate Environment". Confirm the termination.

End Goal:

By the end of this assignment, you should be able to:

    Successfully deploy a Python Django web application to AWS Elastic Beanstalk.
    Understand the basic workflow of creating an Elastic Beanstalk application and environment.
    Identify the key files (requirements.txt, Procfile) needed for deploying a Python application on Elastic Beanstalk.
    Access and verify your deployed application using the environment's URL.
    Monitor the health and status of your Elastic Beanstalk environment.
    Understand the importance of cleaning up resources after use to manage costs.

This exercise provides a foundational understanding of how Elastic Beanstalk simplifies the deployment and management of web applications on AWS. It serves as a stepping stone for exploring more advanced Elastic Beanstalk features and integrating other AWS services with your applications.
