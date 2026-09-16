def WriteMessagesFile(file_descriptor, package, version, printer):
    _WriteFile(file_descriptor, package, version, _Proto2Printer(printer))