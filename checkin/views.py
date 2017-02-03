from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.db import models

# Create your views here.
from django.views.generic import TemplateView
from models import CheckIn

from register.models import Application


def checkInHacker(application):
    checkin = CheckIn()
    checkin.application = application
    checkin.save()


def getNotCheckedInhackersList():
    hackersList = Application.objects.exclude(id__in=[checkin.application for checkin in CheckIn.objects.all()])
    return hackersList


class CheckInListView(LoginRequiredMixin, TemplateView):
    template_name = 'templates/check-in-list.html'
    hackersList = getNotCheckedInhackersList()

    def get_context_data(self, **kwargs):
        context = super(CheckInListView, self).get_context_data(**kwargs)
        context['applications'] = getNotCheckedInhackersList()
        return context


class CheckInHackerView(LoginRequiredMixin, TemplateView):
    template_name = 'templates/check-in-hacker.html'

    def get_context_data(self, **kwargs):
        context = super(CheckInHackerView, self).get_context_data(**kwargs)
        appid = int(kwargs['id'])
        app = Application.objects.filter(id=appid)[0]
        context.update({
            'app': app,
        })
        return context
