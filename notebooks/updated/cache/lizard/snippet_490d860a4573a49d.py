def _format_line(self, side, flag, linenum, text):
    try:
        linenum = '%d' % linenum
        id = ' id="%s%s"' % (self._prefix[side], linenum)
    except TypeError:
        id = ''
    text = text.replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;')
    type_ = 'neutral'
    if '\x00+' in text:
        type_ = 'add'
    if '\x00-' in text:
        if type_ == 'add':
            type_ = 'chg'
        type_ = 'sub'
    if '\x00^' in text:
        type_ = 'chg'
    text = text.replace(' ', '&nbsp;').rstrip()
    return (
        '<td class="diff_lno"%s>%s</td><td class="diff_line diff_line_%s">%s</td>'
         % (id, linenum, type_, text))