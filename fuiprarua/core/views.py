#encoding: utf-8

from django.shortcuts import render, redirect
from forms import ParticipantesForm
from core.models import Participantes

def index(request):
    return render(request, 'index.html')

def registro(request):
    contexto = {}

    form = ParticipantesForm()

    if request.method == "POST":
        form = ParticipantesForm(request.POST)

        if form.is_valid():
            participante = form.save()

    contexto['form'] = form


    return render(request, 'registro.html', contexto)
