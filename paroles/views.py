# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.utils import timezone as tz
from django.core.exceptions import ObjectDoesNotExist

from paroles.models import Parole

def index(request):
    parole = Parole.objects.last_published()
    try:
        prev = Parole.objects.previous_published(parole.date)
    except ObjectDoesNotExist:
        prev = None
    return render(request, 'paroles/index.html',
            {'parole': parole, 'prev': prev})

def parole(request, year, month, day, author_slug, title_slug):
    date = tz.datetime(int(year), int(month), int(day)).date()
    parole = get_object_or_404(Parole, date=date, author_slug=author_slug,
            title_slug=title_slug)
    try:
        prev = Parole.objects.previous_published(parole.date)
    except ObjectDoesNotExist:
        prev = None
    try:
        next = Parole.objects.next_published(parole.date)
    except ObjectDoesNotExist:
        next = None
    return render(request, 'paroles/parole.html',
            {'parole': parole, 'prev': prev, 'next': next})
