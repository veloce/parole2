# *-* coding: utf-8 *-*

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from paroles.models import Parole, ParoleForm

def index(request):
    paroles = Parole.objects.not_published()
    return render(request, 'admin/index.html', {'paroles_to_publish': paroles})

@require_http_methods(['GET', 'POST'])
def add(request):
    if request.method == 'POST':
        form = ParoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin.views.index')
    else:
        form = ParoleForm()

    return render(request, 'admin/add.html', {'form': form})

@require_http_methods(['GET', 'POST'])
def edit(request, id_parole):
    parole = get_object_or_404(Parole, pk=id_parole)

    if request.method == 'POST':
        form = ParoleForm(request.POST, instance=parole)
        if form.is_valid():
            form.save()
            return redirect('admin.views.index')
    else:
        form = ParoleForm(instance=parole)

    return render(request, 'admin/edit.html', {'form': form, 'parole': parole})

@require_http_methods(['POST'])
def delete(request, id_parole):
    parole = get_object_or_404(Parole, pk=id_parole)
    parole.delete()
    messages.info(request, 'La parole a été supprimée.')
    return redirect('admin.views.index')

def logout(request):
    del request.session['openid_username']
    request.session.flush()
    return redirect('/')
