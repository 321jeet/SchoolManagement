from django .shortcuts import render, redirect, HttpResponse
from schl_mng_app.models import Staff, Staff_Notification, Staff_leave, Staff_Feedback, Subject, Session_year, Students, Attendance, Attendance_Report
from django.contrib import messages


def Staff_Home(request):

    return render(request, 'staff/staff_home.html')


def Notificatons(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        notificatons = Staff_Notification.objects.filter(staff_id=staff_id)

        context = {
            'notificatonss': notificatons
        }
        return render(request, 'staff/notification.html', context)

    return render(request, 'staff/notification.html')


def Staff_Mark_As_Done(request, status):
    send_notifiy = Staff_Notification.objects.get(id=status)
    send_notifiy.status = 1
    send_notifiy.save()

    return redirect('staff_notification')


def Staff_Apply_Leave(request):

    staffs = Staff.objects.filter(admin=request.user.id)
    for i in staffs:
        staff_id = i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id=staff_id)

    context = {
        'staff_leave_history': staff_leave_history
    }

    return render(request, 'staff/apply_leave.html', context)


def Staff_Apply_Leave_Save(request):
    if request.method == "POST":
        leave_date = request.POST.get('Leavedate')
        leave_message = request.POST.get('messageleave')
        staff_id = Staff.objects.get(admin=request.user.id)

        leave = Staff_leave(staff_id=staff_id,
                            date=leave_date, messages=leave_message)
        leave.save()
        messages.success(request, 'leave Successfully send')
        return redirect('staff_apply_leave')

    return render(request, 'staff/apply_leave.html')


def Staff_Feedback_view(request):

    staff_id = Staff.objects.get(admin=request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history': feedback_history
    }

    return render(request, 'staff/feedback.html', context)


def Staff_Feedback_Save(request):

    if request.method == "POST":
        feedback = request.POST.get('feedback')
        staff_ids = Staff.objects.get(admin=request.user.id)
        feedback = Staff_Feedback(
            staff_id=staff_ids,
            feedback=feedback,
            feedback_reply=''
        )
        feedback.save()
        print(staff_ids, feedback)
        messages.success(request, 'Feedback Successfully send')
        return redirect('staff_feedback')

    return render(request, 'staff/feedback.html')


def Staff_Take_Attendance(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(Staff=staff_id)

    session_years = Session_year.objects.all()

    action = request.GET.get('action')

    students = None
    get_subject = None
    get_session = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session_year.objects.get(id=session_id)

            subject_student = Subject.objects.filter(id=subject_id)

            for i in subject_student:
                student_id = i.course.id
                students = Students.objects.filter(course_id=student_id)

    context = {
        'subject': subject,
        'session_years': session_years,
        'get_subjects': get_subject,
        'get_sessions': get_session,
        'action': action,
        'students_name': students
    }

    return render(request, 'staff/take_attendance.html', context)


def Staff_Save_Attendance_Student(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_id = request.POST.get('session_id')
        attendance_date = request.POST.get('attendence_date')
        student_id = request.POST.get('student_id')

        get_subject = Subject.objects.get(id=subject_id)
        get_session = Session_year.objects.get(id=session_id)

        attendance = Attendance(
            subject_id=get_subject, attendance_date=attendance_date, session_years_id=get_session
        )
        attendance.save()

        for i in student_id:
            stud_id = i
            p_student = Students.objects.get(id=stud_id)
            attendance_report = Attendance_Report(
                student_id=p_student, attendance_id=attendance)
            attendance_report.save()
        return redirect('staff_take_attendnace')
        
    return render(request, 'staff/take_attendance.html')
   


def Staff_View_Attendance_Student(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(Staff=staff_id)

    session_years = Session_year.objects.all()
    action = request.GET.get('action')

    get_subjects = None
    get_sessions = None
    attendance_date = None
    attendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_ids = request.POST.get('subject_id')
            session_ids = request.POST.get('session_id')
            attendance_date = request.POST.get('attendence_date')

            get_subjects = Subject.objects.get(id=subject_ids)
            get_sessions = Session_year.objects.get(id=session_ids)

            attendance_ss = Attendance.objects.filter(
                subject_id=get_subjects, attendance_date=attendance_date)
            for i in attendance_ss:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(
                    attendance_id=attendance_id)

    context = {
        'subject': subject,
        'session_years': session_years,
        'action': action,
        'get_subject': get_subjects,
        'get_session': get_sessions,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report
    }

    return render(request, 'staff/view_attendance.html', context)
