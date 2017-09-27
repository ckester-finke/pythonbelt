from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

def sessCheck(request):
    try:
        return request.session['user_id']
    except:
        return False

def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    results = User.objects.RegVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    user = User.objects.creator(request.POST)
    messages.success(request, 'User has been created. please log in to continue')
    return redirect('/')

def login(request):
    results = User.objects.logVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    request.session['user_id'] = results['user'].id
    request.session['user_name'] = results['user'].name
    request.session['user_alias'] = results['user'].alias
    return redirect('/home')

def home(request):
    if sessCheck(request) == False:
        return redirect('/')
    current = User.objects.get(id=request.session['user_id'])
    context={
        'friends': current.friend_id.all(),
        'others': User.objects.all().exclude(id=request.session['user_id']).exclude(friend_id=current),
    }
    return render(request, 'login_app/home.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')
def add(request, user_id):
    a1 = User.objects.get(id=request.session['user_id'])
    a2 = User.objects.get(id=user_id)
    a1.friend_id.add(a2)
    a1.save()
    return redirect('/home')
def remove(request, user_id):
    r1 = User.objects.get(id=request.session['user_id'])
    r2 = User.objects.get(id=user_id)
    r1.friend_id.remove(r2)
    r1.save()
    return redirect('/home')
def display(request, user_id):
    if sessCheck(request) == False:
        return redirect('/')
    context={
        'user': User.objects.get(id=user_id),
    }
    return render(request, 'login_app/display.html', context)