from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .algorithm import Gost, Hash, RSA, Signature, DES


def index(request):
    try:
        q = request.POST['question']
        a = request.POST['question']
    except (KeyError):
        return render(request, 'cipher/index.html')
    else:
        return render(request, 'cipher/index.html', {
            'question': q,
            'answer': a,
        })


def gost(request):
    try:
        q = request.POST['question']
        k  =request.POST['key']
    except (KeyError):
        return render(request, 'cipher/gost.html')
    else:
        return render(request, 'cipher/gost.html', {
            'question' : q,
            'key' : k,
            'answer' : Gost.encrypt(q, k)
        })

def des(request):
    try:
        q = request.POST['question']
        k  =request.POST['key']
    except (KeyError):
        return render(request, 'cipher/des.html')
    else:
        return render(request, 'cipher/des.html', {
            'question' : q,
            'key' : k,
            'answer' : DES.encrypt(q, k)
        })

def rsa(request):
    try:
        question = request.POST['question']
        p  =request.POST['p']
        q  =request.POST['q']
    except (KeyError):
        return render(request, 'cipher/rsa.html')
    else:
        return render(request, 'cipher/rsa.html', {
            'question' : question,
            'q' : q,
            'p' : p,
            'answer' : RSA.encrypt(question, p, q)
        })

def hash(request):
    try:
        q = request.POST['input_q']
        p = request.POST['input_p']
        h = request.POST['input_h']
        if not h:
            h=0
        question = request.POST['question']
    except (KeyError):
        return render(request, 'cipher/hash.html')
    else:
        return render(request, 'cipher/hash.html', {
            'input_q':q,
            'input_p':p,
            'input_h':h,
            'question': question,
            'answer': Hash.hash(question, p, q, h),
        })

def sign(request):
    try:
        q = request.POST['input_q']
        p = request.POST['input_p']
        question = request.POST['question']
    except (KeyError):
        return render(request, 'cipher/sign.html')
    else:
        return render(request, 'cipher/sign.html', {
            'input_q':q,
            'input_p':p,
            'question': question,
            'answer': Signature.sign(question, p, q),
        })
