from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from .models import Teacher,Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_dashboard(request):
    a='admin'
    return render(request,'admin-dashboard.html',{'a':a})
 
def student_dashboard(request):
    a=request.session['stud_id']
    b=Student.objects.get(id=a)
    return render(request,'student-dashboard.html',{'b':b})
 
def teacher_dashboard(request):
    a=request.session['tea_id']
    b=Teacher.objects.get(id=a)
    return render(request,'teacher-dashboard.html',{'b':b})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None and user.is_superuser==1:
            return redirect(admin_dashboard)
        elif Student.objects.filter(username=username,password=password).exists():
            stu=Student.objects.filter(username=username,password=password)
            for i in stu:
                if i.Value==1:
                    request.session['stud_id']=i.id
                    return redirect(student_dashboard)
                else:
                    messages.info(request,'Admin Approval Required')
                    return redirect(login)
        elif Teacher.objects.filter(username=username,password=password).exists():
            tea=Teacher.objects.filter(username=username,password=password)
            for i in tea:
                request.session['tea_id']=i.id
                return redirect(teacher_dashboard)
        else:
            messages.info(request,'Password or username incorrect')
            return redirect(login)
    else:
        return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['stud_id']
        return redirect(index)
    except:
        pass
    try:
        del request.session['tea_id']
        return redirect(index)
    finally:
        return redirect(login)
    
def student_register(request):
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        age=request.POST['age']
        gender=request.POST['gender']
        class1=request.POST['class1']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        regno=request.POST['regno']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if Student.objects.filter(username=username).exists():
                messages.warning(request,"Username already exists")
                return redirect(student_register)
            elif Student.objects.filter(regno=regno).exists():
                messages.warning(request,"Registration number already exists")
                return redirect(student_register)
            else:
                stu=Student.objects.create(firstname=firstname,lastname=lastname,age=age,
                                           gender=gender,class1=class1,email=email,regno=regno,
                                           phone=phone,username=username,password=password,Value=0,user_type='student')
                stu.save()
                messages.info(request,'User Added')
                return redirect(student_register)
    else:
        return render(request,'student-registration.html')
    
def student_approval(request):
    student=Student.objects.filter(Value=0)
    return render(request,'student-approval.html',{'student':student})

def approval(request,id):
    stud=Student.objects.get(id=id)
    stud.Value=1
    stud.save()
    messages.success(request,'Approved Successfully!')
    return redirect(student_approval)

def teacher_register(request):
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        age=request.POST['age']
        gender=request.POST['gender']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        uniqueid=request.POST['unid']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if Teacher.objects.filter(username=username).exists():
                messages.warning(request,"Username already exists")
                return redirect(teacher_register)
            elif Teacher.objects.filter(unid=uniqueid).exists():
                messages.warning(request,"Registration number already exists")
                return redirect(teacher_register)
            else:
                Tea=Teacher.objects.create(firstname=firstname,lastname=lastname,age=age,
                                           gender=gender,email=email,unid=uniqueid,
                                           phone=phone,username=username,password=password,user_type='teacher',Value=1)
                Tea.save()
                messages.info(request,'User Added')
                return redirect(teacher_register)
    else:
        return render(request,'teacher-registration.html')
    
#teacher_profile_view
def teacher_profileview(request):
    teaid=request.session["tea_id"]
    data=Teacher.objects.filter(id=teaid)
    return render(request,'teacher-profile.html',{'data':data})

def teacher_profileupdate1(request):
    if request.method=='GET':
        teaid=request.session["tea_id"]
        data=Teacher.objects.filter(id=teaid)
        return render(request,'teacher-profileupdate.html',{"data":data})

def teacher_profileupdate2(request,uid):
    if request.method=='POST':
        teaid=request.session["tea_id"]
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        email=request.POST['email']
        unid=request.POST['unid']
        phone=request.POST['phone']
        password=request.POST['password']
        a=Teacher.objects.filter(id=uid).update(username=username,firstname=fname,lastname=lname,age=age,email=email,unid=unid,phone=phone,password=password)
        messages.info(request,'Profile Updated')
        return redirect(teacher_profileview)
    
#student_profile
def student_profileview(request):
    studid=request.session["stud_id"]
    data=Student.objects.filter(id=studid)
    return render(request,'student-profile.html',{'data':data})

def student_profileupdate1(request):
    if request.method=='GET':
        studid=request.session["stud_id"]
        data=Student.objects.filter(id=studid)
        return render(request,'student-profileupdate.html',{"data":data})
    
def student_profileupdate2(request,uid):
    if request.method=='POST':
        studid=request.session["stud_id"]
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        email=request.POST['email']
        regno=request.POST['regno']
        phone=request.POST['phone']
        password=request.POST['password']
        a=Student.objects.filter(id=uid).update(username=username,firstname=fname,lastname=lname,age=age,email=email,regno=regno,phone=phone,password=password)
        messages.info(request,'Profile Updated')
        return redirect(student_profileview)
    
#admin-teacher_list_view
def teacher_listview(request):
    teacher=Teacher.objects.all()
    return render(request,'teacher-listview.html',{'teacher':teacher})

def teacher_delete(request,uid):
    obj=Teacher.objects.get(id=uid)
    obj.delete()
    messages.success(request,'Data Deleted Successfully')
    return redirect(teacher_listview)

def teacher_edit(request,uid):
    if request.method=='GET':
        tea=Teacher.objects.filter(id=uid)
        return render(request,'teacher-edit.html',{'tea':tea})
    elif request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        ag=request.POST['age']
        phone=request.POST['phone']      
        email=request.POST['email']
        username=request.POST['username']
        unid=request.POST['unid']
        password=request.POST['password']
    x=Teacher.objects.filter(id=uid).update(firstname=fn,lastname=ln,age=ag,unid=unid,phone=phone,email=email,username=username,password=password)
    return redirect(teacher_listview)
   
#admin-student_list_view
def student_listview(request):
    student=Student.objects.filter(Value=1)
    return render(request,'student-listview.html',{'student':student})

def student_delete(request,uid):
    obj=Student.objects.get(id=uid)
    obj.delete()
    messages.success(request,'Data Deleted Successfully')
    return redirect(student_listview)

def student_edit(request,uid):
    if request.method=='GET':
        stud=Student.objects.filter(id=uid)
        return render(request,'student-edit.html',{'stud':stud})
    elif request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        ag=request.POST['age']
        phone=request.POST['phone']      
        email=request.POST['email']
        username=request.POST['username']
        regno=request.POST['regno']
        password=request.POST['password']
    x=Student.objects.filter(id=uid).update(firstname=fn,lastname=ln,age=ag,regno=regno,phone=phone,email=email,username=username,password=password)
    return redirect(student_listview)

