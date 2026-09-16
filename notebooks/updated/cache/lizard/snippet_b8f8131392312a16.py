def MergeVcards(vcard1, vcard2):
    new_vcard = vobject.vCard()
    vcard1_fields = set(vcard1.contents.keys())
    vcard2_fields = set(vcard2.contents.keys())
    mutual_fields = vcard1_fields.intersection(vcard2_fields)
    logger.debug('Potentially conflicting fields: {}'.format(mutual_fields))
    for field in mutual_fields:
        val1 = vcard1.contents.get(field)
        val2 = vcard2.contents.get(field)
        new_values = []
        if not VcardFieldsEqual(val1, val2):
            if field not in MERGEABLE_FIELDS:
                context_str = GetVcardContextString(vcard1, vcard2)
                new_values.extend(SelectFieldPrompt(field, context_str,
                    val1, val2))
            else:
                new_values.extend(VcardMergeListFields(val1, val2))
        else:
            new_values.extend(val1)
        logger.debug('Merged values for field {}: {}'.format(field.upper(),
            u(str(new_values))))
        new_vcard = SetVcardField(new_vcard, field, new_values)
    new_vcard = CopyVcardFields(new_vcard, vcard1, vcard1_fields -
        vcard2_fields)
    new_vcard = CopyVcardFields(new_vcard, vcard2, vcard2_fields -
        vcard1_fields)
    return new_vcard