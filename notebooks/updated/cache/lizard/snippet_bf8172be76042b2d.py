def send_result(pipe, data):
    try:
        pipe.send(data)
    except (pickle.PicklingError, TypeError) as error:
        error.traceback = format_exc()
        pipe.send(RemoteException(error, error.traceback))