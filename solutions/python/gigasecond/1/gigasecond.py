import datetime

def add(moment):
    one_gigasecond_later = moment + datetime.timedelta(seconds=1_000_000_000)

    return one_gigasecond_later
