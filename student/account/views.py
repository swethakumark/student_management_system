from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect,render
from .models import Contact,Course,Coursedeatils,Staff
# Create your views here.
def mainhome(request):
    return render(request,'mainhome.html')
def  login(request):
    return render(request,'signin.html')

def contact(request):
    
    if request.method == 'POST':
   
        if request.POST['name'] is not None:
         
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
    return render(request,'contact.html')

def course(request):
    courses={
        'course':Course.objects.all()
    }
    return render(request,'course.html',courses)

def signup(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phno=request.POST['phno']
        password2=request.POST['password2']
        if password == password2:
            if Staff.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                customer=Staff.objects.create(email = email,name = name,password = password,phno = phno)
                customer.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password is not match')
            return redirect('login')
    else:
        return render(request,'signup.html')
def signin(request):
    if request.method =="POST":
        email =request.POST["email"]
        password=request.POST["password"]
        try:
            check_user=Staff.objects.get(email=email,password=password)
            request.session['email']=check_user.email
            request.session['name']=check_user.name
            request.session['phno']=check_user.phno
            return redirect('loginhome')
        except Staff.DoesNotExist:
            messages.error(request,'inavlid username and password')
            return redirect('signin')             
    return render(request,'signin.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')
def gallery(request):
    return render (request,'gallery.html')
def coursedetails(request):
    name=request.GET['name']
    coursed={
        'coursed':Coursedeatils.objects.filter(name=name).values()
    }
    return render (request,'coursedetails.html',coursed)
def loginhome(request):
        return render (request,'loginhome.html')
def logout(request):
    request.session.pop('email',None)
    request.session.pop('name',None)
    request.session.pop('phno',None)

    return render(request,'signin.html')
