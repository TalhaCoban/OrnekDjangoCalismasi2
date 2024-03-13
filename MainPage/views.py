from django.shortcuts import render, HttpResponse
from django.contrib import messages



def index(request):
    messages.info(request, 'Three credits remain in your account.')
    return render(request, "index.html")
