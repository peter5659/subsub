import json
import os
from django.shortcuts import render


# Create your views here.
def detail(request, storeID) :
    jsonPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'subserve/keys.json')
    print("PATHHHH : ", jsonPath)
    with open(jsonPath, 'r') as f:
        keys = json.load(f)
    mapKey = keys['kakaomap-api']
    return render(request, 'detail.html', {'storeID' : storeID, 'key' : mapKey})


def purchasing(request, storeID) :
    return render(request, 'purchasing.html')