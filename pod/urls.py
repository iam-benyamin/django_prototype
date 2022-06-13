from django.urls import path, re_path
import pod.views as views

urlpatterns = [
    path('description', views.description,
         name="company_description"),
    path('update', views.update,
         name="company_update_web_content"),
]
