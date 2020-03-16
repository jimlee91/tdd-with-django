from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url

from .models import Item, List
# Create your views here.


def home_page(request):
    return render(request, "lists/home.html", {
    })


def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    items = Item.objects.filter(list=list_)
    return render(request, 'lists/list.html', {
        'list': list_
    })


def new_list(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text, list=list_)
        return redirect(resolve_url('lists:view_list', list_.pk))


def add_item(request, pk):
    list_ = List.objects.get(pk=pk)
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text, list=list_)
    return redirect(resolve_url('lists:view_list', list_.pk))
