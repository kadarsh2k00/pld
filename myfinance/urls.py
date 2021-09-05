from django.urls import path

from . import views

app_name = 'myfinance'
urlpatterns = [
    path('', views.index, name='index'),
    path('link_account', views.link_account, name='link-account'),
    path('transactions', views.transactions, name='transactions'),
    path('transactions/get', views.get_transactions, name='get-transactions'),
    path('create_link_token', views.create_link_token, name='create-link-token'),
    path('get_access_token', views.get_access_token, name='get-access-token'),
    path('auth', views.get_auth, name="get-auth"),
    path('signup', views.signup, name="signup"),
    path('create_user', views.create_user, name='create-user'),
    path('log_in', views.log_in, name='log-in'),
    path('log_in_form', views.log_in_form, name='log-in-form'),
    path('log_out', views.log_out, name='log-out'),
    path('refresh_accounts', views.refresh_accounts, name='refresh-accounts')
]