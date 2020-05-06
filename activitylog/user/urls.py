from django.contrib import admin
from django.urls import path, include
from .views import UsersView, MembersActivity

app_name = "user"

urlpatterns = {
    path('all_users/', UsersView.as_view()),
    path('members_record/', MembersActivity.as_view()),
}
