async def handle_student_job_closing(self, container_id, retval):
    try:
        self._logger.debug('Closing student %s', container_id)
        try:
            job_id, parent_container_id, socket_id, write_stream = (self.
                _student_containers_running[container_id])
            del self._student_containers_running[container_id]
        except asyncio.CancelledError:
            raise
        except:
            self._logger.warning(
                'Student container %s that has finished(p1) was not launched by this agent'
                , str(container_id), exc_info=True)
            return
        if job_id in self._student_containers_for_job:
            self._student_containers_for_job[job_id].remove(container_id)
        killed = await self._timeout_watcher.was_killed(container_id)
        if container_id in self._containers_killed:
            killed = self._containers_killed[container_id]
            del self._containers_killed[container_id]
        if killed == 'timeout':
            retval = 253
        elif killed == 'overflow':
            retval = 252
        try:
            await self._write_to_container_stdin(write_stream, {'type':
                'run_student_retval', 'retval': retval, 'socket_id': socket_id}
                )
        except asyncio.CancelledError:
            raise
        except:
            pass
        try:
            await self._docker.remove_container(container_id)
        except asyncio.CancelledError:
            raise
        except:
            pass
    except asyncio.CancelledError:
        raise
    except:
        self._logger.exception('Exception in handle_student_job_closing')