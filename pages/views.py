from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Instructor

def home(request):
    courses = Course.objects.all()[:3]
    instructors = Instructor.objects.all()[:3]

    context = {
        'courses': courses,
        'instructors': instructors

    }

    return render(request, 'pages/home.html', context)


def courses(request):
    courses = Course.objects.all()
    instructors = Instructor.objects.all()

    context = {
        'courses': courses,
        'instructors': instructors

    }

    return render(request, 'pages/courses.html', context)


def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course
    }

    return render(request, 'pages/course.html', context)


def about(request):
    instructors = Instructor.objects.all()
    bestseller = Instructor.objects.all().filter(is_bestseller=True)

    context = {
        'instructors': instructors,
        'bestseller': bestseller

    }

    return render(request, 'pages/about.html', context)

def register(request):
    if request.method == 'POST':
        print('Successfully Reg')
        return redirect('/')
    else:
        return render(request, 'pages/register.html')


def login(request):
    return render(request, 'pages/login.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')