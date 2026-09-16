def generate_events_list(generator):
    if not localized_events:
        generator.context['events_list'] = sorted(events, reverse=True, key
            =lambda ev: (ev.dtstart, ev.dtend))
    else:
        generator.context['events_list'] = {k: sorted(v, reverse=True, key=
            lambda ev: (ev.dtstart, ev.dtend)) for k, v in localized_events
            .items()}