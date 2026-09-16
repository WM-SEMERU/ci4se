def copy_to_clipboard(self, url):
    if url is None:
        self.term.flash()
        return
    try:
        clipboard_copy(url)
    except (ProgramError, OSError) as e:
        _logger.exception(e)
        self.term.show_notification('Failed to copy url: {0}'.format(e))
    else:
        self.term.show_notification(['Copied to clipboard:', url], timeout=1)