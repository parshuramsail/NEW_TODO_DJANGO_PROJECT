from django import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Todo
from .forms import TodoForm
# Create your views here.


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm()
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'app/index.html', page)


def remove(request, id):
    item = Todo.objects.get(pk=id)
    item.delete()
    messages.info(request, "item removed !!")
    return redirect('todo')
