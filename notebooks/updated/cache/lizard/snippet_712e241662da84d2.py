def get_job_amounts(agent, project_name, spider_name=None):
    job_list = agent.get_job_list(project_name)
    pending_job_list = job_list['pending']
    running_job_list = job_list['running']
    finished_job_list = job_list['finished']
    job_amounts = {}
    if spider_name is None:
        job_amounts['pending'] = len(pending_job_list)
        job_amounts['running'] = len(running_job_list)
        job_amounts['finished'] = len(finished_job_list)
    else:
        job_amounts['pending'] = len([j for j in pending_job_list if j[
            'spider'] == spider_name])
        job_amounts['running'] = len([j for j in running_job_list if j[
            'spider'] == spider_name])
        job_amounts['finished'] = len([j for j in finished_job_list if j[
            'spider'] == spider_name])
    return job_amounts