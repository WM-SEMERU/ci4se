def _get_event_and_context(self, event, arg_type):
    eid = _choose_id(event, arg_type)
    ev = self.concept_dict[eid]
    concept, metadata = self._make_concept(ev)
    ev_delta = {'adjectives': [], 'states': get_states(ev), 'polarity':
        get_polarity(ev)}
    context = self._make_context(ev)
    event_obj = Event(concept, delta=ev_delta, context=context)
    return event_obj