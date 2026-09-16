def push_progress(self, status, object_id, progress):
    fastprint(progress_fmt(status, object_id, progress), end='\n')