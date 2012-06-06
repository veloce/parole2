# *-* coding: utf-8 *-*

# Create your views here.
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from parole2.paroles.models import Parole, ParoleForm

def index(request):
    paroles = Parole.objects.not_published()
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

@require_http_methods(['GET', 'POST'])
def edit(request, id_parole):
    parole = get_object_or_404(Parole, pk=id_parole)

    if request.method == 'POST':
        form = ParoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parole2.admin.views.index')
    else:
        form = ParoleForm(instance=parole)

    return render_to_response('admin/edit.html',
            {'form': form, 'parole': parole},
            context_instance=RequestContext(request))

def delete(request, id_parole):
    parole = get_object_or_404(Parole, pk=id_parole)
    parole.delete()
    messages.info(request, 'La parole a été supprimée.')
    return redirect('parole2.admin.views.index')

def logout(request):
    del request.session['openid_username']
    request.session.flush()
    return redirect('/')
