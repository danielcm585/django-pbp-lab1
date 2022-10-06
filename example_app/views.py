from django.shortcuts import render

def index(request):
    context = {
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, 'index.html', context)
