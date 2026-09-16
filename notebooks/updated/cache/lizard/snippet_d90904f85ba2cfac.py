def view_all_work_queues():
    count_list = list(db.session.query(work_queue.WorkQueue.queue_name,
        work_queue.WorkQueue.status, func.count(work_queue.WorkQueue.
        task_id)).group_by(work_queue.WorkQueue.queue_name, work_queue.
        WorkQueue.status))
    queue_dict = {}
    for name, status, count in count_list:
        queue_dict[name, status] = dict(name=name, status=status, count=count)
    max_created_list = list(db.session.query(work_queue.WorkQueue.
        queue_name, work_queue.WorkQueue.status, func.max(work_queue.
        WorkQueue.created)).group_by(work_queue.WorkQueue.queue_name,
        work_queue.WorkQueue.status))
    for name, status, newest_created in max_created_list:
        queue_dict[name, status]['newest_created'] = newest_created
    min_eta_list = list(db.session.query(work_queue.WorkQueue.queue_name,
        work_queue.WorkQueue.status, func.min(work_queue.WorkQueue.eta)).
        group_by(work_queue.WorkQueue.queue_name, work_queue.WorkQueue.status))
    for name, status, oldest_eta in min_eta_list:
        queue_dict[name, status]['oldest_eta'] = oldest_eta
    queue_list = list(queue_dict.values())
    queue_list.sort(key=lambda x: (x['name'], x['status']))
    context = dict(queue_list=queue_list)
    return render_template('view_work_queue_index.html', **context)