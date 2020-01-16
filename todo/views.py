from django.shortcuts import render
from django.http import HttpResponse

from .models import ListWrapper

# Create your views here.

def index(request):
    todoLists = ListWrapper.objects.order_by('-creationDate')
    context = { 'todoLists' : todoLists}
    return render(request, 'todo/index.html', context)

