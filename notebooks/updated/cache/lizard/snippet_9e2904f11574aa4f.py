def _import_csv(self, path):
    if not path:
        return
    try:
        dialect, has_header, digest_types, encoding = (self.main_window.
            interfaces.get_csv_import_info(path))
    except IOError:
        msg = _('Error opening file {filepath}.').format(filepath=path)
        post_command_event(self.main_window, self.StatusBarMsg, text=msg)
        return
    except TypeError:
        return
    return CsvInterface(self.main_window, path, dialect, digest_types,
        has_header, encoding)