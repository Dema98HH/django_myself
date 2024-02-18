from django.db.models import Count
from django.views.generic import ListView
from django.shortcuts import render
from .models import Department

class ArticleListView(ListView):
    template_name = 'department/index.html'
    context_object_name = 'departments'
    paginate_by = 2
    ordering = ['-department_name']

    def get_queryset(self):
        return Department.objects.annotate(employee_count=Count('employee'))

def singular_record(request, pk):
    department = Department.objects.get(id=pk)
    context = {'department': department}
    return render(request, 'department/department.html', context=context)