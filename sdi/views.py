from django.shortcuts import render, redirect


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')


def tourist(request):
    return render(request, 'tourist.html')


def journalist(request):
    return render(request, 'journalist.html')


def citizen_scientist(request):
    return render(request, 'citizen_scientist.html')


def gi_specialist(request):
    return render(request, 'gi_specialist.html')
