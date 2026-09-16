def concurrent_slots(slots):
    for i, slot in enumerate(slots):
        for j, other_slot in enumerate(slots[i + 1:]):
            if slots_overlap(slot, other_slot):
                yield i, j + i + 1