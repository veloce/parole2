# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.utils import timezone as tz

from paroles.models import Parole

def index(request):
    parole = Parole.objects.last_published()
    return render(request, 'paroles/index.html', {'parole': parole})

def parole(request, year, month, day, author_slug, title_slug):
    date = tz.datetime(int(year), int(month), int(day)).date()
    parole = get_object_or_404(Parole, date=date, author_slug=author_slug,
            title_slug=title_slug)
    return render(request, 'paroles/parole.html', {'parole': parole})
