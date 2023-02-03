from django.shortcuts import render,redirect,HttpResponse
from schl_mng_app.models import Students,Student_Notification,Student_leave,Student_Feedback,Subject,Attendance,Attendance_Report,Staff
from django.contrib import messages


def Student_Home(request):

    return render (request,'student/student_home.html')


def Students_Notificatons(request):
    student=Students.objects.filter(admin=request.user.id)
    for i in student:
        student_id=i.id
        notificatons=Student_Notification.objects.filter(student_id=student_id)

        context={
            'notificatonss':notificatons
        }
        return render (request,'student/notification.html',context)
     
    return render (request,'student/notification.html')

def Students_Mark_As_Done(request,status):
    send_notifiy=Student_Notification.objects.get(id=status)
    send_notifiy.status = 1
    send_notifiy.save()

    return redirect('student_notification') 




def Student_Apply_Leave(request):

    student =Students.objects.filter(admin=request.user.id)
    for i in student:
        student_id=i.id

        student_leave_history = Student_leave.objects.filter(student_id=student_id)

    context={
         'student_leave_history':student_leave_history
         }

    return render (request,'student/apply_leave.html',context)    

def Student_Apply_Leave_Save(request):
    if request.method == "POST":
        leave_date=request.POST.get('Leavedate')
        leave_message=request.POST.get('messageleave')
        student_id=Students.objects.get(admin=request.user.id)

        leave_save=Student_leave(student_id=student_id,date=leave_date, messages=leave_message)
        leave_save.save()
        messages.success(request,'leave Successfully send')
        return redirect ('student_apply_leave')

    return render (request,'student/apply_leave.html')        




def Student_Feedback_view(request):

    student_id =Students.objects.get(admin=request.user.id)
    feedback_history =Student_Feedback.objects.filter(student_id=student_id)

    context={
        'feedback_history':feedback_history
    }
    
    return render (request,'student/feedback.html',context)         


def Student_Feedback_Save(request):

    if request.method == "POST":
        feedback=request.POST.get('feedback')
        student_ids=Students.objects.get(admin=request.user.id)
        feedback=Student_Feedback(
            student_id=student_ids,
            feedback=feedback,
            feedback_reply=''
        )
        feedback.save()
        
        messages.success(request,'Feedback Successfully send')
        return redirect ('student_feedback')

    return render (request,'student/feedback.html')        

def Student_View_Attendance(request):
     
    student=Students.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(course=student.course_id)
    action=request.GET.get('action')
    
    attendance_report= None
    get_subject = None
    
    if action is not None:
        if request.method =='POST':
            subject_ids = request.POST.get('subject_id')
            get_subject=Subject.objects.filter(id=subject_ids) 
            attendance_report=Attendance_Report.objects.filter(student_id=student,attendance_id__subject_id=subject_ids)
    context={
        'action':action,
       'subject':subject,
       'get_subject':get_subject,
       'attendance_report':attendance_report,
    

       
         }
    return render (request,'student/show_attendance.html',context)