from django.utils.timezone import localtime, now


def is_visit_long(different, minutes=60):
    return different > minutes * 60


def get_duration(visit):
    entered_time = localtime(visit.entered_at)
    leaved_time = visit.leaved_at
    if leaved_time:
        leaved_time = localtime(leaved_time)
        different = (leaved_time-entered_time).total_seconds()
    else:
        different = (now()-entered_time).total_seconds()
    return different


def format_duration(duration):
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours)} часов {int(minutes)} минут {int(seconds)} секунд'
