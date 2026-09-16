def show_summaries(cls, keys=None, indent=0, *args, **kwargs):

    def find_summary(key, key_txt, doc):
        return '\n'.join(wrapper.wrap(doc[:doc.find('\n\n')]))
    str_indent = ' ' * indent
    wrapper = TextWrapper(width=80, initial_indent=str_indent + ' ' * 4,
        subsequent_indent=str_indent + ' ' * 4)
    return cls._show_doc(find_summary, *args, keys=keys, indent=indent, **
        kwargs)