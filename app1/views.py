from django.shortcuts import render,redirect
from .forms import EventForm
from .models import Organizer_Model
# Create your views here.


def Home(request):
    form=EventForm()
    if request.method=='POST':
        form=EventForm(request.POST)
        form.save()
        form=EventForm()

    data=Organizer_Model.objects.all()

    # else:

    context={
        'form':form,
        'data':data,

    }
    return render(request,'app1/index.html',context)


def Delete_record(request,id):
    # print(id,'11111111111111')
    a=Organizer_Model.objects.get(pk=id)
    a.delete()
    return redirect('/')


def Update_record(request,id):
    if request.method=='POST':
        data=Organizer_Model.objects.get(pk=id)
        form=EventForm(request.POST, instance=data) 
        if form.is_valid():
            form.save()
    else:
        data=Organizer_Model.objects.get(pk=id)
        form=EventForm(instance=data)
    context={
        'form':form,
        # 'data':data,

    }
    return render(request,'app1/update.html',context)