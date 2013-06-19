#encoding: utf-8

from django.forms import ModelForm

from core.models import Participantes

class ParticipantesForm(ModelForm):
    class Meta:
        model = Participantes