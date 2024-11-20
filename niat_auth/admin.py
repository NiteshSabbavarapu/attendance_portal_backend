from django.contrib import admin

from attendance_tracker.models import *
from niat_auth.models.models import AuthToken

admin.site.register(AuthToken)
admin.site.register(Attendance_punch_in_model)
admin.site.register(Attendance_punch_out_model)
