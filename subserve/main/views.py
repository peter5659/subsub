from django.shortcuts import render
import os
import json

# Create your views here.
def main(request):
    return render(request, 'main.html')

def search(request):
    return render(request, 'search.html')

def mylocation(request) :
    jsonPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'subserve/keys.json')
    with open(jsonPath, 'r') as f:
        keys = json.load(f)
    mapKey = keys['kakaomap-api']
    return render(request, 'mylocation.html', {'key' : mapKey})