# from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at__isnull=True):
        entered_time = localtime(visit.entered_at)
        duration = get_duration(visit)
        timer = format_duration(duration)

        active_visit = {
            'who_entered': visit.passcard,
            'entered_at': entered_time,
            'duration': timer
        }

        non_closed_visits.append(active_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)


def format_duration(duration):
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours)} часов {int(minutes)} минут {int(seconds)} секунд'
