def get_new_timesheets_contents(self):
    popular_aliases = self.get_popular_aliases()
    template = ['# Recently used aliases:']
    if popular_aliases:
        contents = '\n'.join(template + [('# ' + entry) for entry, usage in
            popular_aliases])
    else:
        contents = ''
    return contents