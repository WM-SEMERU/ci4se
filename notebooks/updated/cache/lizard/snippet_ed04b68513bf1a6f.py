def get_task(self, course, taskid):
    if not id_checker(taskid):
        raise InvalidNameException('Task with invalid name: ' + taskid)
    if self._cache_update_needed(course, taskid):
        self._update_cache(course, taskid)
    return self._cache[course.get_id(), taskid][0]