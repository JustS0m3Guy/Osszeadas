from atexit import register
import imp
from django.shortcuts import render
from random import randint
# Create your views here.

def index(request):
    pla = randint(1,100)
    plb = randint(1,100)
    plawns = secretcucc(pla,plb)
    template='index.html'
    context={
        'pla':pla,
        'plb':plb,
        'plawns':plawns,
        'plbad1':wrongformula1(pla,plb),
        'plbad2':wrongformula2(pla,plb),
        'plbad3':wrongformula3(pla,plb),
        'questiona':randint(1,100),
        'questionb':randint(1,100),
    }
    if request.method=="POST":
        print(int(request.POST['oldquestiona']))
        print(int(request.POST['oldquestionb']))
        print(int(request.POST['questionawns']))
        print(secretcucc(int(request.POST['oldquestiona']), int(request.POST['oldquestionb']))==int(request.POST['questionawns']))
    return render(request, template, context)

def secretcucc(a,b):
    return 2*a+b

def wrongformula1(a,b):
    return a+b

def wrongformula2(a,b):
    return 2*a+2*b

def wrongformula3(a,b):
    return a*b