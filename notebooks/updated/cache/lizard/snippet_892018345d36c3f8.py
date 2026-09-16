def _fill_text(self, text, width, indent):
    parts = text.split('\n\n')
    for i, part in enumerate(parts):
        if part.startswith('* '):
            subparts = part.split('\n')
            for j, subpart in enumerate(subparts):
                subparts[j] = super(WrappedTextHelpFormatter, self)._fill_text(
                    subpart, width, indent)
            parts[i] = '\n'.join(subparts)
        else:
            parts[i] = super(WrappedTextHelpFormatter, self)._fill_text(part,
                width, indent)
    return '\n\n'.join(parts)