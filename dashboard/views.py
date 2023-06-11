from django.shortcuts import render,get_object_or_404
from item.models import Item
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.



@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user )
    items_sold = Item.objects.filter(Q(created_by=request.user) & Q(is_sold=True) )
    items_sold_count = items_sold.count()
    
    
    profit = 0
    for item in items_sold:
        profit += item.price

    return render(request,'dashboard/index.html',{
        'items':items,
        'items_sold':items_sold_count,
        'profit':profit,
    })

