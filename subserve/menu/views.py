from django.shortcuts import render

# Create your views here.
def detail(request):
    menus=Menu.objects.all()
    menu=Menu()
    menu.menu_name = request.POST.get('menu_name')
    return render(request, 'detail.html', {'menus':menus})
