# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.http import require_http_methods

from parole2.paroles.models import Parole, ParoleForm

def index(request):
    paroles = Parole.objects.all()
    return render_to_response('admin/index.html',
            {'paroles_to_publish': paroles},
            context_instance=RequestContext(request))

@require_http_methods(['GET', 'POST'])
def add(request):
    if request.method == 'POST':
        form = ParoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parole2.admin.views.index')
    else:
        form = ParoleForm()

    return render_to_response('admin/add.html',
            {'form': form},
            context_instance=RequestContext(request))

def logout(request):
    del request.session['openid_username']
    request.session.flush()
    return redirect('/')
