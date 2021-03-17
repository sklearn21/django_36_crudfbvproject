
from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm

# Create your views here.


def retrieve_view(request):
    employees = Employee.objects.all()
    return render(request, 'testapp/index.html', {'employees': employees})


def create_view(request):
    form = EmployeeForm()
    if request.method =='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'testapp/create.html', {'form': form})