from django.contrib import admin

from attendance_tracker.models import *
from niat_auth.models.models import User, UserRole

admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(Attendance_punch_in_model)
admin.site.register(Attendance_punch_out_model)
