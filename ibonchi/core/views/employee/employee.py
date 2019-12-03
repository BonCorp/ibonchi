from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView, CreateView, DeleteView, DetailView

from ibonchi.core.forms import EmployeeForm
from ibonchi.core.models import Employee


class EmployeeList(ListView):
    template_name = 'employee/employee_list.html'
    model = Employee

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'employee/employee_create.html'
    form_class = EmployeeForm
    success_url = 'employees'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(EmployeeCreate, self).form_valid(form)
#
#
@method_decorator(login_required, name='dispatch')
class EmployeeDelete(DeleteView):
    template_name = 'employee/employee_delete.html'
    model = Employee
    success_url = reverse_lazy('employees')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id=id_)
#
#
@method_decorator(login_required, name='dispatch')
class EmployeeUpdate(UpdateView):
    template_name = 'employee/employee_update.html'
    model = Employee
    success_url = reverse_lazy('employees')
    form_class = EmployeeForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Employee, id=id_)
