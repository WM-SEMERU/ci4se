def get_cmd_epilog(self):
    try:
        return self.source.epilog
    except AttributeError:
        pass
    try:
        return '\n'.join(get_localized_docstring(self, self.
            get_gettext_domain()).splitlines()[1:]).split('@EPILOG@', 1)[1
            ].strip()
    except (AttributeError, IndexError, ValueError):
        pass