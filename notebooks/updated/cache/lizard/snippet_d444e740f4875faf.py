def CopyVcardFields(new_vcard, auth_vcard, field_names):
    for field in field_names:
        value_list = auth_vcard.contents.get(field)
        new_vcard = SetVcardField(new_vcard, field, value_list)
    return new_vcard