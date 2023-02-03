from django.urls import path,include
from . import views
from schl_mng_app import hod_views,staff_views,student_views

urlpatterns = [
    path('base',views.base,name="base"),

    path('',views.Login,name="login"),
    path('loginpage',views.LoginPage,name='LoginPage'),
    path('logout',views.LogOut,name="logout"),

    # Profile
    path('profile/',views.Profile,name="profile"),
    path('update_profile/',views.ProfileUpadte,name="update_profile"),

    #  Hod 

    path('hod/home',hod_views.HodHome,name='Hod_Home'),
    path('add_student/',hod_views.Add_Student,name='add_student'),
    path('view_student/',hod_views.View_Student,name='view_student'),
    path('edit_student/<int:id>/',hod_views. Edit_Student,name='edit_student'),
    path('update_student/',hod_views. Update_Student,name='update_student'),
    path('delete_student/<str:admin>/',hod_views. Delete_Student,name='delete_student'),

# staff
    path('add_staff/',hod_views.Add_Staff,name='add_staff'),  
    path('view_staff/',hod_views.View_Staff,name='view_staff'),
    path('edit_staff/<int:id>/',hod_views.Edit_Staff,name='edit_staff'),  
    path('update_staff/',hod_views.Update_Staff,name='update_staff'),
    path('delete_staff/<str:admin>/',hod_views. Delete_Staff,name='delete_staff'),





# Subject  
    path('add_subject/',hod_views.Add_Subject,name='add_subject'),  
    path('view_subject/',hod_views.View_Subject,name='view_subject'),
    path('edit_subject/<int:id>/',hod_views.Edit_Subject,name='edit_subject'),  
    path('update_subject/',hod_views.Update_Subject,name='update_subject'),
    path('delete_subject/<int:id>/',hod_views. Delete_Subject,name='delete_subject'),




#    course
    path('add_course/',hod_views.Add_Course,name='add_course'),
    path('view_course/',hod_views.View_Course,name='view_course'),
    path('edit_course/<int:id>/',hod_views.Edit_Course,name='edit_course'),
    path('update_course/',hod_views. Update_Course,name='update_course'),
    path('delete_course/<int:id>/',hod_views. Delete_Course,name='delete_course'),

#  session years

    path('add_session/',hod_views.Add_Session,name='add_Session'),
    path('view_session/',hod_views.View_Session,name='view_Sesion'),
    path('edit_session/<int:id>/',hod_views.Edit_Session,name='edit_session'),
    path('update_sessio/',hod_views. Update_Session,name='update_session'),
    path('delete_session/<int:id>/',hod_views. Delete_session,name='delete_session'),


#  hod to staff Notification
    path('hod/staff_notification/',hod_views.Send_Staff_Notificatons,name='hod/staff_notification'),
    path('hod/staff_save_notification/',hod_views.Save_Staff_Notificatons,name='hod/staff_save_notification'),
  



    path('hod/student_notification/',hod_views.Send_Student_Notificatons,name='hod/student_notification'),
    path('hod/student_save_notification/',hod_views.Save_Student_Notificatons,name='hod/student_save_notification'),
  

#  hod to  staff leave urls
  
    path('hod_staff_leave_view/',hod_views.Staff_Leave_View,name='hod_staff_leave_view'),
    path('hod_staff_leave_approve/<int:id>/',hod_views.Staff_Leave_Approve,name='hod_staff_leave_approve'),
    path('hod_staff_leave_disapprove/<int:id>/',hod_views.Staff_Leave_Dispprove,name='hod_staff_leave_disapprove'),
 

#  hod to  student leave urls

    path('hod/student_leave_view/',hod_views.Student_Leave_View,name='hod/student_leave_view'),
    path('hod/student_leave_approve/<int:id>/',hod_views.Student_Leave_Approve,name='hod/student_leave_approve'),
    path('hod/student_leave_disapprove/<int:id>/',hod_views.Student_Leave_Dispprove,name='hod/student_leave_disapprove'),
 



# Hod To staff Fedback  urls
    path('hod_staff_feedback_reply/',hod_views.Staff_Feedback_Reply,name='hod_staff_feedback_reply'),
    path('hod_staff_feedback_reply_save/',hod_views.Staff_Feedback_Reply_Save,name='hod_staff_feedback_reply_save'),
 
# Hod To student  Fedback  urls
    path('hod/student_feedback_reply/',hod_views.Student_Feedback_Reply,name='hod_student_feedback_reply'),
    path('hod_student_feedback_reply_save/',hod_views.Student_Feedback_Reply_Save,name='hod_student_feedback_reply_save'),
 
    path('hod/view_attendance/',hod_views.Hod_View_Attendancet,name='hod_view_attendnace'),







   
# Staff Urls 

    path('staff_home/',staff_views.Staff_Home,name='staff_home'),
    path('staff_notification/',staff_views.Notificatons,name='staff_notification'),
    path('staff_notification_markasdone/<str:status>/',staff_views.Staff_Mark_As_Done,name='staff_notification_done'),

    path('staff_leave/',staff_views.Staff_Apply_Leave,name='staff_apply_leave'),
    path('staff_leave_save/',staff_views.Staff_Apply_Leave_Save,name='staff_apply_leave_save'),

    
    path('staff_feedback/',staff_views.Staff_Feedback_view,name='staff_feedback'),
    path('staff_feedback_save/',staff_views.Staff_Feedback_Save,name='staff_feedback_save'),

    
    path('staff/take_attendance/',staff_views.Staff_Take_Attendance,name='staff_take_attendnace'),
    path('staff/save_attendance_student/',staff_views.Staff_Save_Attendance_Student,name='staff_save_student_attendnace'),

    path('staff/View_attendance_student/',staff_views.Staff_View_Attendance_Student,name='staff_view_student_attendnace'),








# student  

    path('student/home/',student_views.Student_Home,name='student_home'),
    path('student/notification/',student_views.Students_Notificatons,name='student_notification'),
    path('student/notification_markasdone/<str:status>/',student_views.Students_Mark_As_Done,name='student_notification_done'),


    path('student/leave/',student_views.Student_Apply_Leave,name='student_apply_leave'),
    path('student/leave_save/',student_views.Student_Apply_Leave_Save,name='student_apply_leave_save'),


 
    path('student/feedback/',student_views.Student_Feedback_view,name='student_feedback'),
    path('student/feedback_save/',student_views.Student_Feedback_Save,name='student_feedback_save'),
    

    path('student/view_attendance/',student_views.Student_View_Attendance,name='student_view_attendnace'),
]


