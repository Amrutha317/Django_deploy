# from django.shortcuts import render
# from django.http import HttpResponse
# clicked = 1
# def index(request) :
#   global clicked
#   clicked += 1
#   my_dict = {'count' : clicked}
#   return render(request, 'index.html', my_dict)


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# 'request' name is convention. It can be some other name too.
from .models import Program, Student
from .forms import StudentForm

clicked = 1


def index(request):
    global clicked
    clicked += 1
    fruits = ['apple', 'banana', 'kiwi', 'guava', 'mango']
    return render(request, 'index.html', context={
        'message': f'{clicked} times',
        'fruits':fruits,
        'program_values': Program.objects.all(),
        'student_values': Student.objects.all()
    })


def help(request) :
    return render(request, 'help.html')

def get_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            s_name = form.cleaned_data['name']
            s_roll = form.cleaned_data['roll']
            s_year = form.cleaned_data['year']
            s_dob = form.cleaned_data['dob']
            s_degree = form.cleaned_data['degree']
            s_branch = form.cleaned_data['branch']
            print(s_name, s_roll, s_year, s_dob, s_degree, s_branch)

            p = Program.objects.filter(title=s_degree, branch=s_branch).first()
            if p:
                Student(program=p, roll_number=s_roll, name=s_name, year=s_year, dob=s_dob).save()
            else:
                np = Program(title=s_degree, branch=s_branch)
                np.save()
                Student(program=np, roll_number=s_roll, name=s_name, year=s_year, dob=s_dob).save()
        return HttpResponseRedirect('/student/')
    else:
        form = StudentForm()
        return render(request, 'StudentForm.html', {'form': form})
