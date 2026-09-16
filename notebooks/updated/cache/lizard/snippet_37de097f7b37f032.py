def fromMarkdown(md, *args, **kwargs):
    return TOC.fromHTML(markdown(md, *args, **kwargs))