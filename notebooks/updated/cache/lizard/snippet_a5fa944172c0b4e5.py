def index(request):
    recent_jobs = JobRecord.objects.order_by('-start_time')[0:100]
    recent_trials = TrialRecord.objects.order_by('-start_time')[0:500]
    total_num = len(recent_trials)
    running_num = sum(t.trial_status == Trial.RUNNING for t in recent_trials)
    success_num = sum(t.trial_status == Trial.TERMINATED for t in recent_trials
        )
    failed_num = sum(t.trial_status == Trial.ERROR for t in recent_trials)
    job_records = []
    for recent_job in recent_jobs:
        job_records.append(get_job_info(recent_job))
    context = {'log_dir': AUTOMLBOARD_LOG_DIR, 'reload_interval':
        AUTOMLBOARD_RELOAD_INTERVAL, 'recent_jobs': job_records, 'job_num':
        len(job_records), 'trial_num': total_num, 'running_num':
        running_num, 'success_num': success_num, 'failed_num': failed_num}
    return render(request, 'index.html', context)