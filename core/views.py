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
    data = {}
    try:
        id_event = request.GET.get('id')
        if id_event:
            event = Event.objects.get(id=id_event)
            if event.user == request.user:
                data['event'] = event
    finally:
        return render(request, 'event.html', data)



@login_required(login_url='/login/')
def subimt_event(request):
    if request.POST:
        id_event = request.POST.get('id_event')
        title = request.POST.get('title')
        event_date = request.POST.get('event_date')
        description = request.POST.get('description')
        user = request.user
        if id_event:
            Event.objects.filter(id=id_event).update(title=title, event_date=event_date, description=description)
        else:
            Event.objects.create(title=title, event_date=event_date, description=description, user=user)
    return redirect('/schedule')


@login_required(login_url='/login/')
def delete_event(request, id_event):
    event = Event.objects.get(id=id_event)
    if request.user == event.user:
        event.delete()
    return redirect('/schedule')
