from django.urls import path
from . import views
urlpatterns =[

    path('api/nothi_app_gen' , views.nothi_application_generator , name ="nothi_application_generator")

]