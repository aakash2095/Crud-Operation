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
        crud=Crudform()
        cd=Crud.objects.all()
        return render (request,'core/base.html',{'crud':crud,'cd':cd})

def delete(request,id):
    if request.method == 'POST':
        cd=Crud.objects.get(pk=id)
        cd.delete()
        return redirect('base')
    
def update(request,id):
    if request.method == 'POST':
        cd=Crud.objects.get(pk=id)
        crud=Crudform(request.POST,instance=cd)
        if crud.is_valid():
            crud.save()
    else:
        cd=Crud.objects.get(pk=id)
        crud=Crudform(instance=cd)
    return render(request,'core/update.html',{'crud':crud})