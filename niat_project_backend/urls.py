"""
URL configuration for niat_project_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from attendance_tracker.views.attendace_report_api import attendance_report_api
from attendance_tracker.views.attendance_info_api import \
    attendance_info_home_page_api
from attendance_tracker.views.punch_in_api import punch_in_api
from attendance_tracker.views.punch_out_api import punch_out_api
from niat_auth.views.user_sign_in_and_sign_up_view import *

urlpatterns = [
    path('admin/', admin.site.urls),

]
