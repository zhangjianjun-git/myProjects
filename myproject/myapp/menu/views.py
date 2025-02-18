from django.shortcuts import render
from ..models import Menu

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menus.html', {'menus': menus})
