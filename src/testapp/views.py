from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'testapp/index.html')

def print_num(request):
    num = {
        'num' : request.POST['num']
    }
    return render(request, 'testapp/print_num.html', num)