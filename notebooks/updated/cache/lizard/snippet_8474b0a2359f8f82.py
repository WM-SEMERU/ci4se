def assimilate(self, path):
    try:
        d = self.get_task_doc(path)
        if self.mapi_key is not None and d['state'] == 'successful':
            self.calculate_stability(d)
        tid = self._insert_doc(d)
        return tid
    except Exception as ex:
        import traceback
        logger.error(traceback.format_exc())
        return False