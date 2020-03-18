from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url

from .models import Item, List
# Create your views here.


def home_page(request):
    return render(request, "lists/home.html", {
    })


def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    if request.method == 'POST':
        Item.objects.create(list=list_, text=request.POST['item_text'])
        return redirect(resolve_url('lists:view_list', list_.pk))

    return render(request, 'lists/list.html', {
        'list': list_
    })


def new_list(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        new_item_text = request.POST['item_text']
        item = Item.objects.create(text=new_item_text, list=list_)
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            list_.delete()
            return render(request, 'lists/home.html', {
                'error': "You can't have an empty list item"
            })

        return redirect(resolve_url('lists:view_list', list_.pk))
