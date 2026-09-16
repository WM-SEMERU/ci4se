def warn_import_error(type_of_obj_support: str, caught: ImportError):
    msg = StringIO()
    msg.writelines('Import Error while trying to add support for ' +
        type_of_obj_support +
        """. You may continue but the associated parsers and converters wont be available : 
"""
        )
    traceback.print_tb(caught.__traceback__, file=msg)
    msg.writelines(str(caught.__class__.__name__) + ' : ' + str(caught) + '\n')
    warn(msg.getvalue())