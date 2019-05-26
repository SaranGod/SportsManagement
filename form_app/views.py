from django.shortcuts import render
from .models import Admin_model,player,Owner_model
import django.contrib.auth.urls as Users
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required

#User.objects.get(username=the_username).pk
@login_required
def form_view(request,*args,**kwargs):
    queryset1=Admin_model.objects.all()
    queryset2=Owner_model.objects.all()
    cont={"objects":queryset1, "objects2":queryset2}
    return render(request,"list.html",cont)



# Create your views here.
def home_view(request,*args,**kwargs):
    queryset1=Admin_model.objects.all()
    queryset2=Owner_model.objects.all()
    cont={"objects":queryset1, "objects2":queryset2}
    return render(request,"base.html",cont)
