from django.shortcuts import render,HttpResponse,redirect
from schl_mng_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from schl_mng_app.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
login_required(login_url='/')
def base(request):
    
    return render(request,"base.html")


def Login(request):
    
    return render(request,"login.html")    
# login_required(login_url='/')
def LoginPage(request):
    if request.method=='POST':
        user=EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
            #  return HttpResponse("email;"+request.POST.get('email')  +'password :'+request.POST.get('password'))  
        if user!=None:
            login(request,user)
            user_type=user.user_type
            if user_type=='1':
                
                return redirect('Hod_Home')
            elif user_type=='2':
                return redirect('staff_home')
            elif user_type=='3':
                return redirect('student_home')
            else:
                 return HttpResponse ("user not found")   
        else:
            messages.error=(request,'email and password are invailid....')
            
        return  redirect('/' )         

def LogOut(request):
     logout(request)

     return  redirect('/')  
     

# login_required(login_url='/')
def Profile (request):
    user=CustomUser.objects.get(id=request.user.id)
    context={
        'user':user
    }

    return render (request,'profile.html',context)

# login_required(login_url='/')
def ProfileUpadte(request):
    if request.method =="POST":

        profile_Pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        # username=request.POST.get('username')
        # email=request.POST.get('email')
        password=request.POST.get('password')
       
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
           
            if password!=None and password!= '':
                customuser.set_password(password)
                
            if profile_Pic!=None and profile_Pic!= '':
                customuser.profile_Pic=profile_Pic   
            customuser.save()

            redirect('profile')    
            messages.success= (request,' your Profile Upadted Successfully')

        except:
            messages.error=(request,' your Profile not update')

    return render(request,'profile.html')        


        

    