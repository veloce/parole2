# Create your views here.
from django.shortcuts import render_to_response

from paroles.models import Parole

def index(request):
    parole = Parole.objects.last_published()
    return render_to_response('pages/index.html', {'parole': parole})
