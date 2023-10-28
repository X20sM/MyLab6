from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'courses']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code']

class AddCourseForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.none())

    def __init__(self, student):
        super().__init__()
        self.fields['course'].queryset = Course.objects.exclude(students=student)