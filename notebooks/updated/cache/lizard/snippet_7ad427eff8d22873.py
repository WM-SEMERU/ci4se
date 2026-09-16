def get_coordinator():
    workflow_queue = Queue.Queue()
    complete_queue = Queue.Queue()
    coordinator = WorkflowThread(workflow_queue, complete_queue)
    coordinator.register(WorkflowItem, workflow_queue)
    return coordinator