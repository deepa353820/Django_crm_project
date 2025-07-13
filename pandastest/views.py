from django.shortcuts import render
from .models import*
import pandas as pd

# Create your views here.
def employees(request):
    item = Employee.objects.all().values()
    df = pd.DataFrame(item)
    dict = df.to_html()
    return render(request,'demo.html',{'dict': dict})
def employees(request):
    qs = Employee.objects.all().values()
    df = pd.DataFrame(qs)
    if df.empty:
        html_table = "<p>No employee data available.</p>"
    else:
        html_table = df.to_html(index=False, classes='table table-striped')
    return render(request, 'demo.html', {'table': html_table})


def employees(request):
    qs = Employee.objects.all().values()
    df = pd.DataFrame(qs)
    
    # Optional: reorder or rename columns
    df = df[['emp_id', 'name', 'rank']]  # avoid the default 'id' if not needed
    # Add Bootstrap classes to the HTML table
    html_table = df.to_html(
        index=False,
        classes='table table-striped table-bordered text-center align-middle',
        border=0
    )
    return render(request, 'demo.html', {'table': html_table})


def test_data(request):
    emp = test.objects.all()
    return render(request,'test.html',{'emp': emp})


def testing(request):
    emp = test.objects.get()
    return render(request,'test.html',{'emp': emp})

