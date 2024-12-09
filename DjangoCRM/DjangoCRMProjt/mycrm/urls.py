
from django.contrib import admin
from django.urls import path
#from mycrm import views
from . import views


urlpatterns = [
    path("", views.home,name='home'),
    path("logout/", views.logout_user,name='logout'),
    path("Register/", views.Register_user, name='Register'),
    path("record/<int:pk>/", views.customer_record, name='record'),
    path("delete/<int:pk>/", views.delete_record, name='delete'),
    path("add_record/", views.add_record, name='add_record'),
    path("update/<int:pk>/", views.update_record, name='update'),

]