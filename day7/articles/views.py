from django.shortcuts import render
from .models import article

# Create your views here.


def home(request):
    data1=article.objects.all().order_by('id')
    context={
        'data1':data1
    }
    return render(request,'index.html',context)
def navigate(request,pk):
    data2=article.objects.get(id=pk)
    context={
        'data2':data2
    }
    return render(request,'navigate.html',context)


