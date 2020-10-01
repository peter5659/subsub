import json
import os
from django.shortcuts import render
from store.models import Store

# Create your views here.
def detail(request, storeID) :
    #store = Store.objects.filter(id = storeID)
    store = Store.objects.get(id= storeID)
    #저장된 매장중에 검색한 매장 찾기
    jsonPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'subserve/keys.json')
    print("PATHHHH : ", jsonPath)
    with open(jsonPath, 'r') as f:
        keys = json.load(f)
    mapKey = keys['kakaomap-api']
    context = {'store' : store, 'key' : mapKey}
    return render(request, 'detail.html', context)
    #return render(request, 'detail.html', {'storeID' : storeID, 'key' : mapKey})


def purchasing(request, storeID) :
    return render(request, 'purchasing.html')