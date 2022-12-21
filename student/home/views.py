from django.shortcuts import render,redirect
from .models import Students
from .forms import StudentForm
from django.views import View
from account.models import Staff,Contact
from django.contrib import messages


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'loginhome.html')

class Form(View):
    def get(self,request):
        forms=StudentForm()
        return render(request,'form.html',{'form':forms})
    def post(self,request):
        if request.method == "POST":
            std1 = StudentForm(request.POST)
            if std1.is_valid():
                std1.save()
                student=Students.objects.all()
                return render(request,'show.html',{'form':student})
            else :
                print("Form not valid")
            return redirect("show")


class Staffs(View):
    def get(self,request):
        customer = Staff.objects.all()
        return render(request,'staff.html',{'form':customer})

class Enquiry(View):
    def get(self,request):
        staff = Contact.objects.all()
        return render(request,'enquiry.html',{'form':staff})
        
class Profile(View):
    def get(self,request):
        if request.session['email'] is not None :
            customer=Staff.objects.filter(email=request.session['email'])
        return render(request,'profile.html',{'customer':customer})

class Delete(View):
    def get(self,request):
        delete=request.GET['delete']
        Students.objects.filter(student_id=delete).delete()
        student=Students.objects.all()
        return render(request,'show.html',{'forms':student})


class Edit(View):
    def get(self,request):
        edit1=request.GET['edit']
        edit=Students.objects.filter(student_id=edit1)
        return render(request,'edit.html',{'forms':edit})
    def post(self,request):
        edit1=request.GET['edit']
        if request.method == 'POST':
            if Students.objects.filter(student_id = edit1).exists():
                if request.POST['student_address']:
                    print(request.POST['student_address'])
                    Students.objects.filter(student_id=edit1).update(student_address=request.POST['student_address'])
                if request.POST['student_place']:
                    Students.objects.filter(student_id=edit1).update(student_place=request.POST['student_place'])
                if request.POST['student_name']:
                    Students.objects.filter(student_id=edit1).update(student_name=request.POST['student_name'])
                if request.POST['student_email']:
                    Students.objects.filter(student_id=edit1).update(student_email=request.POST['student_email'])
                if request.POST['student_phone']:
                    Students.objects.filter(student_id=edit1).update(student_phone=request.POST['student_phone'])
                student=Students.objects.all()
                return render(request,'show.html',{'form':student})

class Editprofile(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1)
        return render(request,'editprofile.html',{'forms':edit})
    def post(self,request):
        edit1=request.session['email']
        if request.method == 'POST':
            if Staff.objects.filter(email=edit1).exists():
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['name']:
                    Staff.objects.filter(email=edit1).update(name=request.POST['name'])
                if request.POST['email']:
                    if Staff.objects.filter(email=request.POST['email']).exists():
                        edit=Staff.objects.filter(email=edit1)
                        messages.errror(request,"email id already exists")
                        return render(request,'editprofile.html',{'forms':edit})
                    else:
                        Staff.objects.filter(email=edit1).update(email=request.POST['email'])
                        request.session['email']=request.POST['email']

                if request.POST['phno']:
                    Staff.objects.filter(email=edit1).update(phno=request.POST['phno'])
                customer=Staff.objects.filter(email=request.session['email'])
                return render(request,'profile.html',{'customer':customer})

class Shows(View):
    def get(self,request):
        student = Students.objects.all()
        return render(request,'show.html',{'forms':student})
    
def forgot(request):
    if request.method == "POST":
        email = request.POST['email']
        password=request.POST['password']
        if Staff.objects.filter(email=email).exists():
            Staff.objects.filter(email=email).update(password=password)
            return redirect('login')
        else:
            messages.error(request,'invalid email id')
            return redirect('forgot')
    return render(request,'forgotpassword.html')
