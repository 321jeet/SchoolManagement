from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from schl_mng_app.models import Course, Session_year, Students, CustomUser, Staff,Subject,Staff_Notification,Staff_leave,Staff_Feedback,Student_Notification,Student_leave,Student_Feedback,Attendance,Attendance_Report
from django.contrib import messages

login_required(login_url='/')
def HodHome(request):
     student_count=Students.objects.all().count()
     course_count=Course.objects.all().count()
     staff_count=Staff.objects.all().count()
     subject_count=Subject.objects.all().count()

     count_gender_male=Students.objects.filter(gender='male').count()
     count_gender_female=Students.objects.filter(gender='female').count()

     context={
        'student_counts':student_count,
        'staff_counts':staff_count,
        'course_counts':course_count,
        'subject_counts':subject_count,
        'gender_male':count_gender_male,
        'gender_female':count_gender_female,



     }

     return render(request, 'hod/home.html',context)

login_required(login_url='/')
def Add_Student(request):
    course = Course.objects.all()
    session_year = Session_year.objects.all()
    if request.method == "POST":
        profile_Pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dateofbirth = request.POST.get('dob')
        course_id = request.POST.get('course_id')
        session_years_id = request.POST.get('session_years_id')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Allready Taken')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Allready Taken')
            return redirect('add_student')

        else:
            user = CustomUser(first_name=first_name, last_name=last_name,
                              username=username, email=email, profile_Pic=profile_Pic, user_type=3)
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_year.objects.get(id=session_years_id)

            studet = Students(
                admin=user,
                gender=gender,
                dateofbirth=dateofbirth,
                course_id=course,
                session_id=session_year,
                father_name=father_name,
                mother_name=mother_name,
                address=address,
                city=city,
                mobile=mobile

            )
            studet.save()
            messages.success(request, 'Student Successfully  Saved')
        return redirect('Hod_Home')
    context = {
        'courses': course,
        'session_years': session_year
    }

    return render(request, 'hod/stdadd.html', context)

login_required(login_url='/')
def View_Student(request):
    students = Students.objects.all()
    context = {
        'student': students
    }

    return render(request, 'hod/view_student.html', context)

login_required(login_url='/')
def Delete_Student(request, admin):
    student_delete = CustomUser.objects.get(id=admin)
    student_delete.delete()
    messages.success(request, 'Student Successfully  deleted')

    return redirect('view_student')

login_required(login_url='/')
def Edit_Student(request, id):
    student_update = Students.objects.filter(id=id)
    course = Course.objects.all()
    session = Session_year.objects.all()
    context = {
        'courses': course,
        'session_years': session,
        'student_updates': student_update
    }
    return render(request, 'hod/student_update.html', context)

login_required(login_url='/')
def Update_Student(request):
    if request.method == "POST":
        profile_Pic = request.FILES.get('profile_pic')
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dateofbirth = request.POST.get('dob')
        course_id = request.POST.get('course_id')
        session_years_id = request.POST.get('session_years_id')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')

        users = CustomUser.objects.get(id=student_id)
        users.first_name = first_name
        users.last_name = last_name
        users.email = email
        users.username = username

        if password != None and password != '':
            users.set_password(password)

        if profile_Pic != None and profile_Pic != '':
            users.profile_Pic = profile_Pic

        users.save()

        student = Students.objects.get(admin=student_id)
        student.gender = gender
        student.dateofbirth = dateofbirth
        student.father_name = father_name
        student.mother_name = mother_name
        student.address = address
        student.city = city
        student.mobile = mobile

        if dateofbirth != None and dateofbirth != '':
            student.dateofbirth = dateofbirth

        courses = Course.objects.get(id=course_id)
        student.course_id = courses

        session_years = Session_year.objects.get(id=session_years_id)
        student.session_id = session_years

        student.save()
        messages.success(request, ' Student Recored  Successfully  Updated')

    return redirect('view_student')

login_required(login_url='/')
def Add_Course(request):
    if request.method == 'POST':
        name = request.POST.get('addcourse')
        add_course = Course(name=name)
        add_course.save()
        messages.success(request, ' Course Successfully  Saved')
        return redirect('add_course')

    return render(request, 'hod/course_add.html')

login_required(login_url='/')
def View_Course(request):

    view_course = Course.objects.all()

    context = {
        'view_courses': view_course
    }

    return render(request, 'hod/view_course.html', context)

login_required(login_url='/')
def Edit_Course(request, id):

    edit_course = Course.objects.filter(id=id)

    context = {
        'edit_course': edit_course
    }

    return render(request, 'hod/update_course.html', context)

login_required(login_url='/')
def Update_Course(request):
    if request.method == 'POST':
        name = request.POST.get('addcourse')
        Course_id = request.POST.get('course_id')

        update = Course.objects.get(id=Course_id)
        update.name = name
        update.save()
        messages.success(request, ' Course Are Successfully  Updated')

        return redirect('view_course')

login_required(login_url='/')
def Delete_Course(request, id):
    delete_courses = Course.objects.get(id=id)
    delete_courses.delete()
    messages.success(request, 'Student Successfully  deleted')
    return redirect('view_course')

login_required(login_url='/')
def Add_Staff(request):
    if request.method == 'POST':
        profile_Pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dateofbirth = request.POST.get('dob')
        address = request.POST.get('address')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Allready Taken')
            return redirect('add_staff')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Allready Taken')
            return redirect('add_staff')

        else:
            user = CustomUser(first_name=first_name, last_name=last_name,
                              username=username, email=email, profile_Pic=profile_Pic, user_type=2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                gender=gender,
                dateofbirth=dateofbirth,
                address=address,
                city=city,
                mobile=mobile

            )
            staff.save()
            messages.success(request, 'Staff Successfully  Saved')
            return redirect('Hod_Home')

    return render(request, 'hod/add_staff.html')

login_required(login_url='/')
def View_Staff(request):
    view_staff = Staff.objects.all()
    context = {
        'view_staffs': view_staff
    }

    return render(request, 'hod/view_staff.html', context)

login_required(login_url='/')
def Edit_Staff(request, id):
    edit_staff = Staff.objects.filter(id=id)
    context = {
        'edit_staffs': edit_staff
    }

    return render(request, 'hod/staff_update.html', context)

login_required(login_url='/')
def Update_Staff(request):

    if request.method == "POST":
        profile_Pic = request.FILES.get('profile_pic')
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dateofbirth = request.POST.get('dob')
        address = request.POST.get('address')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')

        users = CustomUser.objects.get(id=staff_id)
        users.first_name = first_name
        users.last_name = last_name
        users.email = email
        users.username = username

        if password != None and password != '':
            users.set_password(password)

        if profile_Pic != None and profile_Pic != '':
            users.profile_Pic = profile_Pic

        users.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.dateofbirth = dateofbirth
        staff.address = address
        staff.city = city
        staff.mobile = mobile

        staff.save()
        messages.success(request, 'Staff Successfully  Updated')
        return redirect('view_staff')

    return render(request, 'hod/staff_update.html')
login_required(login_url='/')
def Delete_Staff(request, admin):
    delete_staffs = CustomUser.objects.get(id=admin)
    delete_staffs.delete()
    messages.error(request, 'Staff Successfully  Deleted')

    return redirect('view_staff')

login_required(login_url='/')
def Add_Subject(request):
    staff_Name=Staff.objects.all()
    course_Name=Course.objects.all()
    if request.method == 'POST':
        S_name=request.POST.get('S_name')
        course_name=request.POST.get('course_name')
        staff_name=request.POST.get('staff_name')

        course = Course.objects.get(id=course_name)
        staff = Staff.objects.get(id=staff_name)

        subject_add=Subject(S_name=S_name,course=course,Staff=staff)

        subject_add.save()
        messages.success(request, 'Subject Successfully  saved')
        return redirect('view_subject')
    context={
        'staff_names':staff_Name,
        'course_names':course_Name
    }

    return render(request,'hod/add_subject.html',context)

login_required(login_url='/')
def View_Subject(request):
    
    suject_view =Subject.objects.all()

    context={
        'subject_view':suject_view,
           }

    return render(request,'hod/view_subject.html',context)    

login_required(login_url='/')
def Edit_Subject(request,id):
    staff_Name=Staff.objects.all()
    course_Name=Course.objects.all()
    edit=Subject.objects.filter(id=id)
    context={
        'staff_name':staff_Name,
        'edits':edit,
        'course_name':course_Name
    }

    return render (request,'hod/update_subject.html',context) 

login_required(login_url='/')   
def Update_Subject(request):
    if request.method=='POST':
        S_name=request.POST.get('S_name')
        subject_id=request.POST.get('subject_id')
        course_id=request.POST.get('course_name')
        staff_id=request.POST.get('staff_name')
        
        course_name=Course.objects.get(id=course_id)
        staff_name=Staff.objects.get(id=staff_id)

        subject_up=Subject.objects.get(id=subject_id)
        subject_up.S_name=S_name
        subject_up.course=course_name
        subject_up.Staff=staff_name
        subject_up.save()
        messages.success(request, 'Subject Are Successfully  Updated')
        return redirect('view_subject') 
    return render(request,'hod/update_subject.html')    

login_required(login_url='/')
def Delete_Subject(request,id):
    delete_sub=Subject.objects.get(id=id)
    delete_sub.delete()
    messages.success(request, 'Subject Are Successfully  deleted')

    return redirect('view_subject')   

login_required(login_url='/')     
def Add_Session(request):
    if request.method == 'POST':
        session_start=request.POST.get('session_start')
        session_end=request.POST.get('session_end')
        
        session_years=Session_year(session_start=session_start,session_end=session_end)
        session_years.save()
        messages.success(request, 'Sessions Are Successfully  Saved')
        return redirect ('view_Sesion')
    return render (request,'hod/add_session.html')

login_required(login_url='/')
def View_Session(request):

    view_sesion=Session_year.objects.all()
    context={
     'view_session':view_sesion
    }

    return render(request,'hod/view_session.html',context)   

login_required(login_url='/')
def Edit_Session(request,id):
    edit_sesion=Session_year.objects.filter(id=id)
    context={
        'edit_session':edit_sesion
    }
    return render (request,'hod/update_session.html',context)

login_required(login_url='/')
def Update_Session(request):
    if request.method =='POST':
        session_start=request.POST.get('session_start')
        session_id=request.POST.get('session_id')
        session_end=request.POST.get('session_end')
        session_years_id=Session_year.objects.get(id=session_id)

        session_years_id.session_start=session_start
        session_years_id.session_end=session_end
        session_years_id.save()
        messages.success(request, 'Sessions Are Successfully  Updated')
        return redirect ('view_Sesion')
    return render (request,'hod/update_session.html')

login_required(login_url='/')
def Delete_session(request,id):

     delete_sesion=Session_year.objects.get(id=id)
     delete_sesion.delete()
     messages.success(request, 'Sessions Are Successfully  deleted')
     return redirect ('view_Sesion')

login_required(login_url='/')
def Send_Staff_Notificatons(request):
    staff_names=Staff.objects.all()
    see_message=Staff_Notification.objects.all().order_by('-id')[0:5]
        
    context={
        'staff_names':staff_names,
        'message_see':see_message

    }

    return render (request,'hod/staff_notification.html',context)    

login_required(login_url='/')
def Save_Staff_Notificatons(request):
    if request.method == 'POST':
        staff_id=request.POST.get('staff_id')
        message=request.POST.get('messages')
        
        staff=Staff.objects.get(id=staff_id)
       
        notification=Staff_Notification(staff_id=staff,message=message)
        notification.save()
        messages.success(request, 'Notifications send successfully ..!')
        return redirect ('hod/staff_notification')


login_required(login_url='/')    
def Staff_Leave_View(request):
    staff_leave =Staff_leave.objects.all()
    context={
        'staff_leave':staff_leave
    }

    return render(request,'hod/staff_leave.html',context)       

login_required(login_url='/')       
def Staff_Leave_Approve(request,id):
    leave=Staff_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('hod_staff_leave_view')

           
login_required(login_url='/')       
def Staff_Leave_Dispprove(request,id):
    leave=Staff_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
   
    return redirect('hod_staff_leave_view')
        
        
def Staff_Feedback_Reply(request):
   
    feedback=Staff_Feedback.objects.all()
    context={
        'feedback':feedback
    }

    

    return render (request,'hod/staff_feedback.html',context)       


def Staff_Feedback_Reply_Save(request):
    if request.method == 'POST':
        feeback_id=request.POST.get('feedback_id')
        feeback_reply=request.POST.get('feedback_reply')
        feedback_staff=Staff_Feedback.objects.get(id=feeback_id)
        feedback_staff.feedback_reply=feeback_reply
        feedback_staff.save()
        return redirect ('hod_staff_feedback_reply')

    return render (request,'hod/staff_feedback.html')



def Send_Student_Notificatons(request):
    student_names=Students.objects.all()
    see_message=Student_Notification.objects.all().order_by('-id')[0:5]
        
    context={
        'student_names':student_names,
        'message_see':see_message

    }

    return render (request,'hod/student_notification.html',context)    

def Save_Student_Notificatons(request):
    if request.method == 'POST':
        student_id=request.POST.get('student_id')
        message=request.POST.get('messages')
        
        student=Students.objects.get(id=student_id)
       
        notification=Student_Notification(student_id=student,message=message)
        notification.save()
        messages.success(request, 'Notifications send successfully ..!')
        return redirect ('hod/student_notification')


def Student_Leave_View(request):
    student_leave =Student_leave.objects.all()
    context={
        'student_leave':student_leave
    }

    return render(request,'hod/student_leave.html',context)  

def Student_Leave_Approve(request,id):
    leave=Student_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('hod/student_leave_view')

           
login_required(login_url='/')       
def Student_Leave_Dispprove(request,id):
    leave=Student_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
   
    return redirect('hod/student_leave_view')    


        
def Student_Feedback_Reply(request):
   
    feedback=Student_Feedback.objects.all()
    context={
        'feedback':feedback
    }

    

    return render (request,'hod/student_feedback.html',context)       


def Student_Feedback_Reply_Save(request):
    if request.method == 'POST':
        feeback_id=request.POST.get('feedback_id')
        feeback_reply=request.POST.get('feedback_reply')
        feedback_staff=Student_Feedback.objects.get(id=feeback_id)
        feedback_staff.feedback_reply=feeback_reply
        feedback_staff.save()
        return redirect ('hod_student_feedback_reply')

    return render (request,'hod/student_feedback.html')


def Hod_View_Attendancet (request):
    
    
    subject = Subject.objects.all()
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
        'attendance_report': attendance_report,
        # 'subject_staff':subject_staff,

    }
    return render (request,'hod/student_attendance.html',context)