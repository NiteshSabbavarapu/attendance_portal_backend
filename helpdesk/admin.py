from django.contrib import admin
from helpdesk.models import UserAccount, UserRole, AttendanceDetails

admin.site.register(UserAccount)
admin.site.register(UserRole)
admin.site.register(AttendanceDetails)
