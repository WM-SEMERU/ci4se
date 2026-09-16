def _format_markdown_requisite(state, stateid, makelink=True):
    fmt_id = '{0}: {1}'.format(state, stateid)
    if makelink:
        return ' * [{0}](#{1})\n'.format(fmt_id, _format_markdown_link(fmt_id))
    else:
        return ' * `{0}`\n'.format(fmt_id)