from django.shortcuts import render,redirect
from . models import Crud
from . forms import Crudform

# Create your views here.

def base(request):
    if request.method == 'POST':
        crud=Crudform(request.POST)
        if crud.is_valid():
            crud.save()
        return redirect('base')
    else:
        crud=Crudform
        return render (request,'core/base.html',{'crud':crud})

