from django.shortcuts import render, redirect
from .forms import DropdownModelForm
from .models import DropdownModel
# Create your views here.


def home(request):
    the_list = DropdownModel.objects.all()
    context = {'the_list':the_list}
    return render(request, 'dropdown/home.html', context)

def chaform(request):
    form = DropdownModelForm(request.POST)
    if request.method == 'POST':
        form.save()
        return redirect('dropdown:home')
    else:
        form = DropdownModelForm()
    context = {
        'form':form
    }

    return render(request, 'dropdown/add.html', context)