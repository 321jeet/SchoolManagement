from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class usermodel (UserAdmin):
    list_display=['username','user_type']

# class studentmodel (UserAdmin):
#     list_display=['first_name','last_name']


admin.site.register(CustomUser,usermodel)
admin.site.register(Students)
admin.site.register(Course)
admin.site.register(Session_year)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Student_Notification)
admin.site.register(Staff_Notification)
admin.site.register(Student_leave)
admin.site.register(Staff_leave)
admin.site.register(Staff_Feedback)
admin.site.register(Student_Feedback)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)