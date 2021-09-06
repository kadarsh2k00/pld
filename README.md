# Plaid_Django_App

Project Features:
1) User signup, login, logout APIs.
2) Token exchange API: An authenticated user can submit a plaid public token that he gets post link integration.
3) This public token is exchanged for access token on the backend.
4) This initiates an async job on the backend for fetching account and item metadata for the access token.
5) Expose a webhook for handling plaid transaction updates and fetch the transactions on receival of a webhook.
6) Expose an api endpoint for fetching all transaction and account data each for a user.
7) Do appropriate plaid error handling.

<h1>Getting Started</h1>
<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>

<h2>Prerequisites</h2>
<p>You will need API keys, which you can receive by signing up in the Plaid Dashboard.</p>
<code>https://dashboard.plaid.com/team/keys</code>

<h2>Installing</h2>
<h4>Open terminal in project folder to create and run virtual environment</h4>
<code>python -m venv ./venv</code><br>
<code>venv\scripts\activate.bat</code><br>

<h2> Install Dependencies</h2>
<code>pip install -r requirements.txt</code><br><br>

<h2>Create a database and write the credentials in settings.py file of moneymanager app</h2>
<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'NAME OF DATABASE',
        'USER': 'postgres',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost'
    }
 }
</pre>

<h2>Now make migrations to create schema in database</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>To use admin panel you need to create superuser</h2>
<code>python manage.py createsuperuser</code>

<h2>Enter the Plaid API credentials in secret_keys.py file</h2>
<pre>
PLAID_CLIENT_ID = 'YOUR CLIENT ID'
PLAID_ENV = 'PLAID ENVIRONMENT'
PLAID_SECRET = 'YOUR SECRET KEY'
</pre>

<h2> To run the program in local server use the following command</h2>
<code>python manage.py runserver</code>

<p>Run local server at http://localhost:8000 or http://127.0.0.1:8000/</p>

<h2>Work Flow</h2>
<h3>Home Page</h3>
<div align="center">
    <img src="https://github.com/kadarsh2k00/Plaid_Django_App/blob/961881a60527d14880d9882e0da5d53d1903c633/Plaid_Django_Demo/Home.png" width="100%"</img> 
</div>

<h3>Registration Page</h3>
<div align="center">
    <img src="https://github.com/kadarsh2k00/Plaid_Django_App/blob/961881a60527d14880d9882e0da5d53d1903c633/Plaid_Django_Demo/SignUp.png" width="100%"</img> 
</div>

<h3>Login Page</h3>
<div align="center">
    <img src="https://github.com/kadarsh2k00/Plaid_Django_App/blob/961881a60527d14880d9882e0da5d53d1903c633/Plaid_Django_Demo/LogIn.png" width="100%"</img> 
</div>

<h3>Landing Page</h3>
<div align="center">
    <img src="https://github.com/kadarsh2k00/Plaid_Django_App/blob/961881a60527d14880d9882e0da5d53d1903c633/Plaid_Django_Demo/Landing.png" width="100%"</img> 
</div>

<h3>All Transactions</h3>
<div align="center">
    <img src="https://github.com/kadarsh2k00/Plaid_Django_App/blob/961881a60527d14880d9882e0da5d53d1903c633/Plaid_Django_Demo/AllTransactions.png" width="100%"</img> 
</div>

<h2>Contributor</h2>
<blockquote>
  Adarsh Kumar<br>
  Email: adarshkmr0605@gmail.com
</blockquote>

<div align="center">
    <h3>====Thank You!====</h3>
</div>
