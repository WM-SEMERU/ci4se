def run(self):
    self.OnStartup()
    try:
        while True:
            message = self._in_queue.get()
            if message is None:
                break
            try:
                self.HandleMessage(message)
            except Exception as e:
                logging.warning('%s', e)
                self.SendReply(rdf_flows.GrrStatus(status=rdf_flows.
                    GrrStatus.ReturnedStatus.GENERIC_ERROR, error_message=
                    utils.SmartUnicode(e)), request_id=message.request_id,
                    response_id=1, session_id=message.session_id, task_id=
                    message.task_id, message_type=rdf_flows.GrrMessage.Type
                    .STATUS)
                if flags.FLAGS.pdb_post_mortem:
                    pdb.post_mortem()
    except Exception as e:
        logging.error('Exception outside of the processing loop: %r', e)
    finally:
        logging.fatal('The client has broken out of its processing loop.')
        os.kill(os.getpid(), signal.SIGKILL)