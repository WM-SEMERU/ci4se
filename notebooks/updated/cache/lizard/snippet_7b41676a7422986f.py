def job_path(cls, project, location, job):
    return google.api_core.path_template.expand(
        'projects/{project}/locations/{location}/jobs/{job}', project=
        project, location=location, job=job)