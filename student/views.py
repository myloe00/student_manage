from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .models import Teacher
from django.views import View
from .forms import StudentForm, OrmModelForm
# Create your views here.

def index(request):
    words = 'World!'
    students = Student.objects.all()
    return render(request, 'index.html', context={'students': students})


class IndexView(View):

    # 以get形式访问会执行get函数,一般情况下获取数据
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        return render(request, 'index.html', context={'students': students})

    # 以post形式访问的话会执行post函数，一般情况下发送数据
    def post(self, request, *args, **kwargs):
        students = Student.objects.all()
        return render(request, 'index.html', context={'students': students})


class StudentView(View):

    # 以get形式访问会执行get函数,一般情况下获取数据
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        form = StudentForm()
        return render(request, 'index.html', context={'students': students, 'form': form})

    # 以post形式访问的话会执行post函数，一般情况下发送数据
    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'error.html', context={'errors': form.errors})
        return HttpResponseRedirect(reverse('student_index'))


class OrmModelView(View):
    def get(self, request, *args, **kwargs):
        form = OrmModelForm()
        students = [student.to_dict() for student in Student.objects.all()]
        teachers = [teacher.to_dict() for teacher in Teacher.objects.all()]
        return render(request, 'OrmModelDemo.html', context={'students': students, 'teachers': teachers, 'form': form})

    def post(self, request, *args, **kwargs):
        students = [student.to_dict() for student in Student.objects.all()]
        teachers = [teacher.to_dict() for teacher in Teacher.objects.all()]
        Student.objects.filter()
        query_data = request.POST.get('query_data')
        loc = locals()
        exec(f"result = {query_data}")
        result = loc['result']
        result = [record.to_dict() for record in result]
        return render(request, 'OrmModelDemo.html', context={
            'students': students, 'teachers': teachers, "query_data": 'XXXXXXX', 'result': result})
