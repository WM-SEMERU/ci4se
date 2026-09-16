def check_decade_apostrophes_long(text):
    err = 'dates_times.dates'
    msg = "Apostrophes aren't needed for decades."
    regex = "\\d\\d\\d0's"
    return existence_check(text, [regex], err, msg)