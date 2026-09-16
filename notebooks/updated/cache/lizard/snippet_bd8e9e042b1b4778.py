def roll_qtrday(other, n, month, day_option, modby=3):
    months_since = other.month % modby - month % modby
    if n > 0:
        if (months_since < 0 or months_since == 0 and other.day <
            _get_day_of_month(other, day_option)):
            n -= 1
    elif months_since > 0 or months_since == 0 and other.day > _get_day_of_month(
        other, day_option):
        n += 1
    return n