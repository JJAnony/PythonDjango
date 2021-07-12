from django.shortcuts import render, HttpResponse
from core.models import Event


# Create your views here.

def hello(requests, name):
    return HttpResponse('<h1>Hello {}</h1>'.format(name))


def list_events(requests):
    event = Event.objects.filter(user=requests.user)
    response = {'events': event}
    return render(requests, 'schedule.html', response)
