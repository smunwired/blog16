from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from .models import Details
from .forms import detailsform

def index(request):
    return render(request,'index.html')
 
def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        obj=Details.objects.create(name=name,age=age,address=address)
        obj.save()
        return redirect('/')

def retrieve(request):
    details=Details.objects.all()
    return render(request,'retrieve.html',{'details':details})

def edit(request,id):
    object=Details.objects.get(id=id)
    return render(request,'edit.html',{'object':object})
    
def update(request,id):
    object=Details.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        if 'add' in request.POST:
            object.pk = None
            form.save()
            object=Details.objects.all()
            return redirect('retrieve')
        if 'update' in request.POST:
            form.save()
            object=Details.objects.all()
            return redirect('retrieve')

def delete(request,pk):   
    Details.objects.filter(id=pk).delete()
    return redirect('retrieve')
