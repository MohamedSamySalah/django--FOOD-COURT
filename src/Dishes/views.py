from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from .models import Dishes,Resturants
from .models import category
# Create your views here.

def Restaurant_list(request):
    Restaurant = Resturants.objects.all()
    context = {'RES_name':Restaurant}
    return render(request,'Dishes/Restaurant_list.html',context)



def Restaurant_items(request,slug):
    # REs_id = Resturants.objects.get(id=id)
    # print(REs_id)
    #  board = get_object_or_404(Board,pk=board_id)
    # return render(request,'topics.html',{'board':board})
    # category = category.objects.all()
    Restaurant = get_object_or_404(Resturants,slug=slug)
    
    context={'RES':Restaurant,}
    return render(request,'Dishes/Restaurant_details.html',context)

