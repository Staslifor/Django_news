from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def politics(request):
    return render(request, 'main/politics.html')


def economy(request):
    return render(request, 'main/economy.html')

