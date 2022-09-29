from django.shortcuts import render

def index(request):
    context = {
        'last_login': request.COOKIES['last_login']
    }
    return render(request, 'index.html', context)
