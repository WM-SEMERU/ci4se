def process_net_command(self, py_db, cmd_id, seq, text):
    meaning = ID_TO_MEANING[str(cmd_id)]
    method_name = meaning.lower()
    on_command = getattr(self, method_name.lower(), None)
    if on_command is None:
        cmd = py_db.cmd_factory.make_error_message(seq, 
            'unexpected command ' + str(cmd_id))
        py_db.writer.add_command(cmd)
        return
    py_db._main_lock.acquire()
    try:
        cmd = on_command(py_db, cmd_id, seq, text)
        if cmd is not None:
            py_db.writer.add_command(cmd)
    except:
        if (traceback is not None and sys is not None and 
            pydev_log_exception is not None):
            pydev_log_exception()
            stream = StringIO()
            traceback.print_exc(file=stream)
            cmd = py_db.cmd_factory.make_error_message(seq, 
                """Unexpected exception in process_net_command.
Initial params: %s. Exception: %s"""
                 % ((cmd_id, seq, text), stream.getvalue()))
            if cmd is not None:
                py_db.writer.add_command(cmd)
    finally:
        py_db._main_lock.release()