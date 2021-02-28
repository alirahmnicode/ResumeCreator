from django.urls import path
from .views import *

app_name = "resume"

urlpatterns = [
    path('edit' , edit_resume , name="edit_resume"),
    path('edit/profile' , edit_profile , name="edit_profile"),
    path('add/skill' , add_skills , name="add_skill"),
    path('add/work' , add_work , name="add_work"),
    path('add/education' , add_education , name="add_education"),
    
    path('<str:name>' , resume , name="userreaume"),
]