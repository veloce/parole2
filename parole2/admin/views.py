# Create your views here.
from django.shortcuts import render_to_response, redirect

from parole2.paroles.models import Parole

def index(request):
    paroles = Parole.objects.all()
    return render_to_response('admin/index.html', {'paroles_to_publish': paroles})

def logout(request):
    del request.session['openid_username']
    request.session.flush()
    return redirect('/')
