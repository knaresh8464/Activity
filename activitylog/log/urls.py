from django.contrib import admin
from django.urls import path, include
from .views import LogView, LogUpdateView

app_name = "log"

urlpatterns = {
    path('all_logs/', LogView.as_view()),
    path('log_end_time/<slug:s_num>/', LogUpdateView.as_view()),
}
