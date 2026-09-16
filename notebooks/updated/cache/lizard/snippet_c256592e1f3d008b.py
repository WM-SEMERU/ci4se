def enqueue_job(request, queue_index, job_id):
    queue_index = int(queue_index)
    queue = get_queue_by_index(queue_index)
    job = Job.fetch(job_id, connection=queue.connection)
    if request.method == 'POST':
        queue.enqueue_job(job)
        if job.get_status() == JobStatus.DEFERRED:
            registry = DeferredJobRegistry(queue.name, queue.connection)
            registry.remove(job)
        elif job.get_status() == JobStatus.FINISHED:
            registry = FinishedJobRegistry(queue.name, queue.connection)
            registry.remove(job)
        messages.info(request, 'You have successfully enqueued %s' % job.id)
        return redirect('rq_job_detail', queue_index, job_id)
    context_data = {'queue_index': queue_index, 'job': job, 'queue': queue}
    return render(request, 'django_rq/delete_job.html', context_data)