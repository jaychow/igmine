from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hubchallenge(request):
    hc = request.GET.get('hc')
    print hc
    return HttpResponse(hc)
