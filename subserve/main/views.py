

from django.shortcuts import render
import os
import json
from store.models import Store
from menu.models import Menu
# Create your views here.
def main(request):
    stores=Store.objects.all()
    # store=Store()
    # store.storename = request.POST.get('storename')
    # store.description = request.POST.get('description')
    return render(request, 'main.html', {'stores' : stores} )


def search(request):
    stores=Store.objects.all().order_by('-id')
    menus = Menu.objects.all().order_by('-menu_id')
    q = request.POST.get('q',"")

    if q:
        stores=stores.filter(storename__icontains=q)
        menus= menus.filter(menu_name__icontains=q)
        return render(request, 'search.html', {'stores' : stores, 'menus' : menus, 'q' : q})
    else:
            return render(request, 'search.html')

def mylocation(request) :
    jsonPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'subserve/keys.json')
    with open(jsonPath, 'r') as f:
        keys = json.load(f)
    mapKey = keys['kakaomap-api']
    return render(request, 'mylocation.html', {'key' : mapKey})

def login(request) :
    return render(request, 'login.html')
