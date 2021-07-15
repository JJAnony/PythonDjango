from django.shortcuts import render, HttpResponse, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def hello(request, name):
    return HttpResponse('<h1>Hello {}</h1>'.format(name))


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou Senha Invalidos')
    return redirect('/login')


@login_required(login_url='/login/')
def list_events(request):
    event = Event.objects.filter(user=request.user)
    response = {'events': event}
    return render(request, 'schedule.html', response)


@login_required(login_url='/login/')
def event(request):
    return render(request, 'event.html')


@login_required(login_url='/login/')
def subimt_event(request):
    if request.POST:
        title = request.POST.get('title')
        event_date = request.POST.get('event_date')
        description = request.POST.get('description')
        user = request.user
        Event.objects.create(title=title, event_date=event_date, description=description, user=user)
    return redirect('/schedule')
