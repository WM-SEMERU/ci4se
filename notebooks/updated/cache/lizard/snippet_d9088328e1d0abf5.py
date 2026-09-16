def renderInTable(self, relpath=''):
    cachekey, html = self.checkCache('InTable', relpath)
    if html is not None:
        return html
    if len(self.imgrec) == 1:
        rec = self.imgrec[0]
        html = '    <TR><TD COLSPAN=2>'
        html += self.renderLinkComment(relpath) or ''
        html += '</TD></TR>\n'
        html_img, comment = self._renderImageRec(rec, relpath, include_size
            =True)
        html += '\n'.join(['    <TR>', '      <TD>%s</TD>' % html_img, 
            '      <TD>%s</TD>' % comment, '    </TR>\n'])
    else:
        html = '    <TR><TD COLSPAN=2>'
        html += self.renderLinkComment(relpath)
        html += (
            """
      <DIV ALIGN=right><P>%s FITS cube, %d planes are given below.</P></DIV></TD></TR>
"""
             % (self.cubesize, len(self.imgrec)))
        for irec, rec in enumerate(self.imgrec):
            html_img, comment = self._renderImageRec(rec, relpath)
            comment = '<P>Image plane #%d.</P>%s' % (irec, comment)
            html += '\n'.join(['    <TR>', '      <TD>%s</TD>' % html_img, 
                '      <TD>%s</TD>' % comment, '    </TR>\n'])
    return self.writeCache(cachekey, html)