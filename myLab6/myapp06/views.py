from django.shortcuts import render,redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm,AddCourseForm

def students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()
        return redirect('students')
    else:
        form = StudentForm()
    students = Student.objects.all()
    return render(request, 'myapp06/students.html', {'students': students, 'form': form})

def courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        form.save()
        return redirect('courses')
    else:
        form = CourseForm()
    courses = Course.objects.all()
    return render(request, 'myapp06/courses.html', {'courses': courses, 'form': form})
def details(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)
        student.courses.add(course)
        return redirect('details', student_id=student.id)
    else:
        form = AddCourseForm(student)
    return render(request, 'myapp06/details.html', {'student': student, 'form': form})
