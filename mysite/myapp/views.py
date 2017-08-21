from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import Course, User,Student,Module
from django.shortcuts import get_object_or_404
from django.urls import reverse
from myapp.forms import StudentForm,LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    courselist = Course.objects.all().order_by('title')[:10]
    return render(request, 'myapp/index.html', {'courselist': courselist})

def detail(request, course_no):
    coursedetail = Course.objects.get(course_no=course_no)
    title= coursedetail.title
    content=coursedetail.overview
    date=coursedetail.created
    instructor=coursedetail.owner
    return render(request,'myapp/website-course.html',{'coursedetail':coursedetail,'title':title,'content':content,'date':date,'instructor':instructor})

def directory_grid(request):
    courselist = Course.objects.all().order_by('title')[:10]

    return render(request,'myapp/grid.html', {'courselist': courselist})

def directory_list(request):
    courselist = Course.objects.all().order_by('title')[:10]
    return render(request,'myapp/list.html', {'courselist': courselist})

def register(request):
    if request.method == 'POST':
        stuform = StudentForm(request.POST)
        if stuform.is_valid():
            user=stuform.save(commit=False)
            user.set_password(stuform.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('myapp:index'))
    else:
        form=StudentForm()
        return render(request,'myapp/sign-up.html',{'form':form,'requset':request.user.username})

def mycourses(request):
        l = len(Student.objects.filter(username=request.user.username))
        if l == 1:
            student = Student.objects.get(username=request.user.username)
            course = student.courses_enrolled.all()

            return render(request, 'myapp/mycourses.html', {'course': course, 'flag': 0, 'name': request.user.username})
        else:

            return render(request, 'myapp/mycourses.html', {'flag': 1})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:mycourses')) #
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        form=LoginForm()
        return render(request, 'myapp/login.html',{'request':request.user,'form':form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))


def take_course(request,course_no):
    l = len(Student.objects.filter(username=request.user.username))
    if l == 1:
        student = Student.objects.get(username=request.user.username)
        course = Course.objects.get(course_no=course_no)
        course.students.add(student)
        modules=Module.objects.get(course__course_no=course_no)

        return render(request, 'myapp/website-take-course.html', {'modules':modules,'course': course, 'flag': 0, 'name': request.user.username})
    else:

        return render(request, 'myapp/website-take-course.html', {'flag': 1})