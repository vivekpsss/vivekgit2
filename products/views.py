from django.shortcuts import render
from .models import Items
from.forms import Empform
# Create your views here.
def index(request):
    obj=Items.objects.all()
    return render(request,'index.html',{"example":obj})

def about(request):
    stu=Empform()
    return render(request,"form.html",{'forms':stu})