from django.shortcuts import render
from .models import FormItems,Test1,Test2
from .forms import Forms1
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#User.objects.get(username=the_username).pk
@login_required
def form_view(request,*args,**kwargs):
    queryset1=Test1.objects.all()
    queryset2=Test2.objects.all()
    cont={"objects":queryset1,"objects2":queryset2}
    return render(request,"list.html",cont)


def form_enter(request,*args,**kwargs):
    form1=Forms1()
    if request.method == "POST":
        form1=Forms1(request.POST)
    #form_data=form1.fields["aadhaar"]
    cont={"form1":form1}
    return render(request,"enter.html",cont)
# Create your views here.
