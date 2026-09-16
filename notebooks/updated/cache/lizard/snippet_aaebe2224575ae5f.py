def generate_error_message(tag, err_uniq, err_appl, err_mult):
    err = []
    if err_uniq:
        err.append('Uniqueness restriction: item type %s' % tag.item_type)
    if err_appl:
        err.append('Applicability restriction: field %s' % tag.field)
    if err_mult:
        err.append('Multiplicity restriction: field %s' % tag.field)
    return err