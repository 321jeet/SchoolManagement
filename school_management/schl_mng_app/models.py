from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    user=( (1,"HOD"),(2,'Staff'),(3,"Student"))
    user_type=models.CharField(choices=user,max_length=120 ,default=1)
    profile_Pic=models.ImageField(upload_to='profile_pic')


class Course(models.Model):
    name=models.CharField(max_length=120)    
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.name

class Session_year(models.Model):
    session_start=models.CharField(max_length=120)   
    session_end=models.CharField(max_length=120)    
    
    def __str__(self) :
        return self.session_start+" "+'To '+self.session_end  

class Students(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE ,default=1)
    dateofbirth=models.CharField(max_length=100 ,default='')
    gender=models.CharField(max_length=100)
    course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING ,default=1 )
    session_id=models.ForeignKey(Session_year,on_delete=models.DO_NOTHING ,default=1)
    father_name=models.CharField(max_length=100, default='')
    mother_name=models.CharField(max_length=100)
    address=models.TextField(default=" ")
    city=models.CharField( max_length=120,default=" ")
    mobile=models.CharField(max_length=13)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.admin.first_name +''+ self.admin.last_name


class Staff(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE ,default=1)
    dateofbirth=models.CharField(max_length=100 ,default='')
    gender=models.CharField(max_length=100)
    address=models.TextField(default=" ")
    city=models.CharField( max_length=120,default=" ")
    mobile=models.CharField(max_length=13)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.admin.username        



class Subject(models.Model):
    S_name=models.CharField(max_length=120)
    course=models.ForeignKey(Course,on_delete=models.CASCADE  )
    Staff=models.ForeignKey(Staff,on_delete=models.CASCADE )
    created_at=models.DateTimeField(auto_now_add=True )
    update_at=models.DateTimeField(auto_now_add=True)

  
    def __str__(self) :
        return self.S_name


class Staff_Notification(models.Model):
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True ,default=0)

    def __str__(self) -> str:
        return self.staff_id.admin.first_name + ' '+self.staff_id.admin.last_name
    
class Staff_leave(models.Model):

    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    messages=models.TextField()
    status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + ' '+self.staff_id.admin.last_name
    
class Staff_Feedback(models.Model):
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.staff_id.admin.first_name 
    


class Student_Notification(models.Model):
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True ,default=0)

    def __str__(self) -> str:
        return self.student_id.admin.first_name + ' '+self.student_id.admin.last_name
   
   
class Student_leave(models.Model):

    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    messages=models.TextField()
    status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name + ' '+self.student_id.admin.last_name
    

    
class Student_Feedback(models.Model):
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.student_id.admin.first_name 


class Attendance(models.Model):
    subject_id=models.ForeignKey (Subject,on_delete=models.DO_NOTHING)
    attendance_date=models.CharField(max_length=100)
    session_years_id=models.ForeignKey(Session_year,on_delete=models.DO_NOTHING)    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_id.S_name 

class Attendance_Report(models.Model):
    student_id=models.ForeignKey (Students,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name 

