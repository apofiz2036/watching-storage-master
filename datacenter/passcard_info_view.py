from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import now, localtime
from django.shortcuts import get_object_or_404


def format_duration(duration):
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours)} часов {int(minutes)} минут {int(seconds)} секунд'


def is_visit_long(different, minutes=60):
    return different > minutes * 60


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []

    for visit in Visit.objects.filter(passcard=passcard):
        entered_time = localtime(visit.entered_at)
        leaved_time = visit.leaved_at
        if leaved_time:
            leaved_time = localtime(leaved_time)
            different = (leaved_time-entered_time).total_seconds()
        else:
            different = (now()-entered_time).total_seconds()

        if is_visit_long(different):
            this_passcard_visits.append({
                'entered_at': entered_time,
                'duration': format_duration(different),
                'is_strange': True
            })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
