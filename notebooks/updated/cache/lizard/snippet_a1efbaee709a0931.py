def store_object(file_name, save_key, file_location, object_to_store=None):
    file = __os.path.join(file_location, file_name)
    try:
        shelve_store = __shelve.open(file)
    except Exception as e:
        LOGGER.critical(
            'Function store_object Error {error} ignoring any errors'.
            format(error=e))
        print('Bad storage dB, rebuilding!!')
        __os.remove(file)
        shelve_store = __shelve.open(file)
    shelve_store[save_key] = object_to_store
    shelve_store.close()