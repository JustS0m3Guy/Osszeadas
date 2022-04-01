from atexit import register
import imp
from django.shortcuts import render
from random import randint
import random
# Create your views here.

def index(request):
    pla = randint(1,10)
    plb = randint(1,10)
    questiona = randint(1,10)
    questionb = randint(1,10)
    plawns = secretcucc(pla,plb)
    list1=[wrongformula1(questiona,questionb),wrongformula2(questiona,questionb),wrongformula3(questiona,questionb),secretcucc(questiona, questionb)]
    shuffledList = random.sample(list1, len(list1))
    template='index.html'
    context={
        'pla':pla,
        'plb':plb,
        'plawns':plawns,
        'list1':shuffledList,
        'questiona':questiona,
        'questionb':questionb,
        'user_awnsered': request.method!="GET",
    }
    if request.method=="POST":
        oldquestiona = int(request.POST['oldquestiona'])
        oldquestionb = int(request.POST['oldquestionb'])
        oldquestionawns_from_user = int(request.POST['awnser'])
        correct_oldawns = oldquestionawns_from_user(oldquestiona, oldquestionb)

        # print(regifela)
        # print(regifelb)
        # print(regifelmo_user_szerint)
        # print(regifelmo_valojaban)

        context['correct'] = oldquestionawns_from_user == correct_oldawns
    return render(request, template, context)

def secretcucc(a,b):
    return 2*a+b

def wrongformula1(a,b):
    return a+b

def wrongformula2(a,b):
    return 2*a+2*b

def wrongformula3(a,b):
    return a*b