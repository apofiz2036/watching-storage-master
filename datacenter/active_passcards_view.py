from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    all_passcards = Passcard.objects.all()
    active_passcards = []
    for passcard in Passcard.objects.filter(is_active=True):
        active_passcards.append(passcard)

    context = {
        'active_passcards': active_passcards,
    }
    return render(request, 'active_passcards.html', context)
