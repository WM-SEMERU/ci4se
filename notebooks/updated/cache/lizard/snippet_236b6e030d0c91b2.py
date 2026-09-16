def write_items(self, calendar):
    for item in self.items:
        event = Event()
        for ifield, efield in ITEM_EVENT_FIELD_MAP:
            val = item.get(ifield)
            if val is not None:
                event.add(efield, val)
        calendar.add_component(event)