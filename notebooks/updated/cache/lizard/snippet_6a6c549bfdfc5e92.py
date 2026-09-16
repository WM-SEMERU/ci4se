def _press_special_key(self, key, down):
    key_code = special_key_translate_table[key]
    ev = (NSEvent.
        otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_
        (NSSystemDefined, (0, 0), 2560 if down else 2816, 0, 0, 0, 8, 
        key_code << 16 | (10 if down else 11) << 8, -1))
    Quartz.CGEventPost(0, ev.Quartz.CGEvent())