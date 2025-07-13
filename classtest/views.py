from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from django.shortcuts import redirect
from .forms import*
from .models import*

# Create your views here.

#to get all data
# def class_data(request):
#     em = tests.objects.all()
#     return render(request,'test_fail.html',{'em':em})


# used this function for filters
# def test_data(request):
#     em = tests.objects.get()
#     return render(request,'test_fail.html',{'em': em})

# used this function for update

# def update_data(request):
#     if request.method == 'POST':
#         form = test_forms(request.POST)
#         if form.is_valid():
#             data = form.save()
#             return render(request, 'test_suceed.html', {'data': data})
#         else:
#             # If POST and form is invalid, show form again with errors
#             return render(request, forms, {'form': form})
#     else:
#         # If GET request, show empty form
#         form = test_forms()
#         return render(request, 'test_fail.html', {'form': form})


# def update_data(request):
#     all_data = tests.objects.all()
#     return render(request,'test_suceed.html',{'all_data':all_data})


def update_data(request):
    if request.method == 'POST':
        form = test_forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_data')  # This should match your URL pattern name
    else:
        form = test_forms()

    all_data = tests.objects.all()
    return render(request, 'test_suceed.html', {'form': form, 'all_data': all_data})


def view_data(request):
    try:
        all_data = tests.objects.all()
    except tests.Http404:
        all_data = None
        return render(request,'data_view.html',{'all_data':all_data})
    
