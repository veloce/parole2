# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone as tz

from paroles.models import Parole

def index(request):
    parole = Parole.objects.last_published()
    return render_to_response('paroles/index.html', {'parole': parole})

def parole(request, year, month, day, slug):
    date = tz.datetime(int(year), int(month), int(day)).date()
    parole = get_object_or_404(Parole, date=date, slug=slug)
    return render_to_response('paroles/parole.html', {'parole': parole})
