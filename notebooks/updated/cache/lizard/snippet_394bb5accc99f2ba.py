def get_keys_to_mods(conn):
    mm = xproto.ModMask
    modmasks = [mm.Shift, mm.Lock, mm.Control, mm._1, mm._2, mm._3, mm._4,
        mm._5]
    mods = conn.core.GetModifierMapping().reply()
    res = {}
    keyspermod = mods.keycodes_per_modifier
    for mmi in range(0, len(modmasks)):
        row = mmi * keyspermod
        for kc in mods.keycodes[row:row + keyspermod]:
            res[kc] = modmasks[mmi]
    return res