def select_event(event=None, selection='ejets'):
    if selection == 'ejets':
        if 0 < len(event.el_pt) < 2 and len(event.jet_pt) >= 4 and len(event
            .ljet_m) >= 1:
            return True
        else:
            return False