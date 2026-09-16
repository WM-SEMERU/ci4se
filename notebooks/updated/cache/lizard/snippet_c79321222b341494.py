def make_slot_check(wanted):
    if isinstance(wanted, types.FunctionType):
        return wanted
    if isinstance(wanted, int):
        item, meta = wanted, None
    elif isinstance(wanted, Slot):
        item, meta = wanted.item_id, wanted.damage
    elif isinstance(wanted, (Item, Block)):
        item, meta = wanted.id, wanted.metadata
    elif isinstance(wanted, str):
        item_or_block = get_item_or_block(wanted, init=True)
        item, meta = item_or_block.id, item_or_block.metadata
    else:
        try:
            item, meta = wanted
        except TypeError:
            raise ValueError('Illegal args for make_slot_check(): %s' % wanted)
    return lambda slot: item == slot.item_id and meta in (None, slot.damage)