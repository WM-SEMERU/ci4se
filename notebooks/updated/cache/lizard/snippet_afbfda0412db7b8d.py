def visit_snippet_latex(self, node):
    code = node.rawsource.rstrip('\n')
    lang = self.hlsettingstack[-1][0]
    linenos = code.count('\n') >= self.hlsettingstack[-1][1] - 1
    fname = node['filename']
    highlight_args = node.get('highlight_args', {})
    if 'language' in node:
        lang = node['language']
        highlight_args['force'] = True
    if 'linenos' in node:
        linenos = node['linenos']

    def warner(msg):
        self.builder.warn(msg, (self.curfilestack[-1], node.line))
    hlcode = self.highlighter.highlight_block(code, lang, warn=warner,
        linenos=linenos, **highlight_args)
    self.body.append(
        """
{\\colorbox[rgb]{0.9,0.9,0.9}{\\makebox[\\textwidth][l]{\\small\\texttt{%s}}}}
"""
         % (fname.replace('_', '\\_'),))
    if self.table:
        hlcode = hlcode.replace('\\begin{Verbatim}',
            '\\begin{OriginalVerbatim}')
        self.table.has_problematic = True
        self.table.has_verbatim = True
    hlcode = hlcode.rstrip()[:-14]
    hlcode = hlcode.rstrip() + '\n'
    self.body.append('\n' + hlcode + '\\end{%sVerbatim}\n' % (self.table and
        'Original' or ''))
    raise nodes.SkipNode