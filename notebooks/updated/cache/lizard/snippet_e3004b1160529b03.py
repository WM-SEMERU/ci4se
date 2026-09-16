def number_of_interactions(records, direction=None):
    if direction is None:
        return len(records)
    else:
        return len([r for r in records if r.direction == direction])