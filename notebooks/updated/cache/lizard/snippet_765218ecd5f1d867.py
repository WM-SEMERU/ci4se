def WaitForTask(task, raiseOnError=True, si=None, pc=None, onProgressUpdate
    =None):
    if si is None:
        si = vim.ServiceInstance('ServiceInstance', task._stub)
    if pc is None:
        pc = si.content.propertyCollector
    progressUpdater = ProgressUpdater(task, onProgressUpdate)
    progressUpdater.Update('created')
    filter = CreateFilter(pc, task)
    version, state = None, None
    while state not in (vim.TaskInfo.State.success, vim.TaskInfo.State.error):
        try:
            version, state = GetTaskStatus(task, version, pc)
            progressUpdater.UpdateIfNeeded()
        except vmodl.fault.ManagedObjectNotFound as e:
            print('Task object has been deleted: %s' % e.obj)
            break
    filter.Destroy()
    if state == 'error':
        progressUpdater.Update('error: %s' % str(task.info.error))
        if raiseOnError:
            raise task.info.error
        else:
            print('Task reported error: ' + str(task.info.error))
    else:
        progressUpdater.Update('completed')
    return state